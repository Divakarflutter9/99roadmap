
@login_required
def download_roadmap_pdf(request, roadmap_id):
    roadmap = get_object_or_404(Roadmap, id=roadmap_id)
    
    # Check if user has initialized payment or if roadmap is free? 
    # Logic: User must be enrolled to download? Or just logged in?
    # Requirement says "add a floating download pdf button". 
    # Usually requires premium access for premium roadmaps.
    
    # Security Check: Ensure user has valid access to this premium resource
    if roadmap.is_premium:
        # Check if user has active subscription
        has_subscription = False
        try:
            if hasattr(request.user, 'subscription') and request.user.subscription.is_active():
                has_subscription = True
        except Exception:
            pass
            
        # Check for direct purchase
        has_purchase = False
        from payments.models import Payment
        has_purchase = Payment.objects.filter(
            user=request.user,
            roadmap=roadmap,
            status='success'
        ).exists()
        
        if not (has_subscription or has_purchase):
            messages.error(request, "You need a Pro subscription or purchase to download the Roadmap PDF.")
            return redirect('roadmap_detail', slug=roadmap.slug)

    if not roadmap.pdf_file:
         messages.error(request, "No PDF available for this roadmap.")
         return redirect('roadmap_detail', slug=roadmap.slug)

    try:
        # Open the original PDF
        input_pdf = PdfReader(roadmap.pdf_file.path)
        output_pdf = PdfWriter()

        # Create watermark
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # Watermark settings
        text = "99Roadmap"
        can.setFont("Helvetica-Bold", 60)
        can.setFillColor(Color(0.5, 0.5, 0.5, 0.2)) # Grey, 20% opacity
        
        # Add watermark diagonally across the page
        can.saveState()
        can.translate(300, 400)
        can.rotate(45)
        can.drawCentredString(0, 0, text)
        can.restoreState()
        
        can.save()
        packet.seek(0)
        
        watermark = PdfReader(packet)
        watermark_page = watermark.pages[0]

        # Apply watermark to each page
        for page in input_pdf.pages:
            page.merge_page(watermark_page)
            output_pdf.add_page(page)

        # Return response
        pdf_buffer = io.BytesIO()
        output_pdf.write(pdf_buffer)
        pdf_buffer.seek(0)
        
        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{roadmap.slug}_99roadmap.pdf"'
        return response
        
    except Exception as e:
        print(f"PDF Error: {e}")
        messages.error(request, "Error generating PDF.")
        return redirect('roadmap_detail', slug=roadmap.slug)
