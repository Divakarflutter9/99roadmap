"""
Cashfree Payment Gateway Integration
"""

import requests
import hashlib
import hmac
import uuid
from django.conf import settings
from datetime import datetime


class CashfreePayment:
    """Cashfree API integration class"""
    
    def __init__(self):
        self.app_id = settings.CASHFREE_APP_ID
        self.secret_key = settings.CASHFREE_SECRET_KEY
        self.env = settings.CASHFREE_ENV
        
        if self.env == 'PRODUCTION':
            self.base_url = 'https://api.cashfree.com/pg'
        else:
            self.base_url = 'https://sandbox.cashfree.com/pg'
    
    
    def create_order(self, order_id, amount, customer_details, return_url, notify_url):
        """
        Create a payment order with Cashfree
        """
        # Dev Mode: If keys are missing, return dummy success
        if not self.app_id or not self.secret_key:
            return {
                'cf_order_id': f'DUMMY_{order_id}',
                'payment_session_id': f'session_{order_id}',
                'order_status': 'ACTIVE',
                'order_token': 'dummy_token'
            }
        
        url = f'{self.base_url}/orders'
        
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-api-version': '2023-08-01',
            'x-client-id': self.app_id,
            'x-client-secret': self.secret_key,
        }
        
        payload = {
            'order_id': order_id,
            'order_amount': float(amount),
            'order_currency': 'INR',
            'customer_details': customer_details,
            'order_meta': {
                'return_url': return_url,
                'notify_url': notify_url,
            },
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            if not response.ok:
                try:
                    error_details = response.json()
                except ValueError:
                    error_details = response.text
                return {'error': f"HTTP {response.status_code}: {error_details}"}
                
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': f"Request Failed: {str(e)}"}
    
    def get_order_status(self, order_id):
        """
        Get the status of a payment order
        """
        # Dev Mode: Always return PAID for dummy orders
        if not self.app_id or not self.secret_key:
            return {
                'cf_order_id': f'DUMMY_{order_id}',
                'order_status': 'PAID',
                'payment_status': 'SUCCESS'
            }
        
        url = f'{self.base_url}/orders/{order_id}'
        
        headers = {
            'Accept': 'application/json',
            'x-api-version': '2023-08-01',
            'x-client-id': self.app_id,
            'x-client-secret': self.secret_key,
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=30)
            if not response.ok:
                try:
                    error_details = response.json()
                except ValueError:
                    error_details = response.text
                return {'error': f"HTTP {response.status_code}: {error_details}"}

            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': f"Request Failed: {str(e)}"}
    
    def verify_signature(self, post_data, signature):
        """
        Verify webhook signature from Cashfree
        
        Args:
            post_data: Request POST data
            signature: Signature from request header
        
        Returns:
            Boolean indicating if signature is valid
        """
        
        # Sort parameters for signature generation
        sorted_keys = sorted(post_data.keys())
        sign_str = ''
        for key in sorted_keys:
            sign_str += f'{key}{post_data[key]}'
        
        # Generate HMAC SHA256 signature
        computed_signature = hmac.new(
            self.secret_key.encode('utf-8'),
            sign_str.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        
        return computed_signature == signature
