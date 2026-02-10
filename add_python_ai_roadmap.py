
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_python_ai_roadmap():
    """Create Python for AI Roadmap"""
    
    print("🚀 Initializing Python for AI Roadmap Creation...")
    
    # 1. Get Category
    # 'cs-engineering'
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='cs-engineering',
        defaults={'name': 'Computer Science & Engineering'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'python-for-ai'
    roadmap_title = 'Python for Artificial Intelligence'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'From Python basics to deploying Deep Learning models. Master NumPy, Pandas, Scikit-Learn, PyTorch, and MLOps.',
            'description': 'A complete roadmap for BTech students to master AI using Python. Covers Data Science foundations, Machine Learning algorithms, Deep Learning with PyTorch/TensorFlow, and industry-grade model deployment.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 120,
            'is_premium': True,
            'is_featured': True,
            'is_active': True,
            'price': 499
        }
    )
    
    if created:
        print(f"✅ Created Roadmap: {roadmap.title}")
    else:
        print(f"ℹ️  Roadmap '{roadmap.title}' already exists. Updating details...")
        # Optional: Clear existing stages if you want a fresh start
        # roadmap.stages.all().delete()
        # print("   ♻️  Cleared existing stages for fresh import.")
        pass # deciding not to delete for now, just append if missing or let manual cleanup happen

    # Clear stages for fresh import to ensure order and content are correct
    roadmap.stages.all().delete()
    print("   ♻️  Cleared existing stages for fresh import.")
        
    # ==========================================
    # STAGE 1: FREE (TEASER) - Python & Data Foundations
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='FREE: Python & Data Foundations',
        description='Essential Python skills for Data Science.',
        order=1,
        is_free=True
    )
    
    topics_s1 = [
        {
            'title': 'Python Refresher for AI',
            'content': """# Core Python Concepts (5-10 Hours)

*   **One-line Explanation:** Quick review of Python features used heavily in data science (Lists, Dictionaries, Comprehensions).
*   **Skills Learned:** Writing vector-friendly code, handling data structures efficiently.
*   **Required Data:** None (Syntax practice).
*   **Tools/Libraries:** Python 3.x, Jupyter Notebook, VS Code.
*   **Hands-On Tasks:**
    *   Create a list comprehension to filter even numbers from a list of 100 integers.
    *   Write a dictionary function to count word frequency in a dummy text string.
    *   Build a simple Class `Dataset` that stores data and returns its shape.
*   **Interview Questions:**
    *   What is the difference between a List and a Tuple? (Mutable vs Immutable)
    *   How does a Dictionary look up values? (Hash Map)
    *   Explain List Comprehension vs For Loop performance. (Comprehension is generally faster/cleaner)
""",
            'order': 1
        },
        {
            'title': 'NumPy Basics',
            'content': """# Numerical Python (5 Hours)

*   **One-line Explanation:** The fundamental package for scientific computing with Python.
*   **Skills Learned:** Matrix operations, broadcasting, vectorization.
*   **Required Data:** Synthetic random data generated via `np.random`.
*   **Tools/Libraries:** NumPy.
*   **Hands-On Tasks:**
    *   Create a 3x3 matrix of random numbers and calculate its dot product with the identity matrix.
    *   Reshape a 1D array of 12 elements into a 3x4 matrix.
    *   Perform element-wise addition of two arrays of different shapes (Broadcasting).
*   **Interview Questions:**
    *   Why is NumPy faster than Python Lists? (Contiguous memory, C implementation)
    *   What is Broadcasting? (Arithmetic on arrays of different shapes)
    *   How do you reverse a 1D array in NumPy? (`arr[::-1]`)
""",
            'order': 2
        },
        {
            'title': 'Pandas Introduction',
            'content': """# Data Manipulation (10 Hours)

*   **One-line Explanation:** High-performance data structures (DataFrames) for data analysis.
*   **Skills Learned:** Loading data (CSV), cleaning missing values, filtering rows.
*   **Required Data:** **Titanic Dataset** (CSV with columns: Age, Fare, Survived, Class). Source: Kaggle/Seaborn.
*   **Tools/Libraries:** Pandas.
*   **Hands-On Tasks:**
    *   Load the Titanic CSV and display the first 5 rows (`head()`).
    *   Filter passengers who are female AND older than 30.
    *   Replace missing values in the 'Age' column with the mean age of all passengers.
*   **Interview Questions:**
    *   What is the difference between `loc` and `iloc`? (Label vs Integer Index)
    *   How do you handle missing data in Pandas? (Drop or Fill/Impute)
    *   Explain the `groupby` function. (Split, Apply, Combine)
""",
            'order': 3
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")
    
    # Teacher Tip for Stage 1
    # "Tip: Run a live coding session where you analyze 'Netflix top movies' data to hook students immediately."


    # ==========================================
    # STAGE 2: BEGINNER - Foundational ML
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Beginner: Foundational ML',
        description='First steps into predicting the future.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'Data Visualization (EDA)',
            'content': """# Seeing the Data (6-8 Weeks Stage Estimate)

*   **One-line Explanation:** Understanding data distributions and relationships through plots.
*   **Skills Learned:** Identifying outliers, trends, and correlations.
*   **Required Data:** **Iris Dataset** (Sepal/Petal lengths). Source: Scikit-learn/UCI.
*   **Tools/Libraries:** Matplotlib, Seaborn.
*   **Hands-On Tasks:**
    *   Plot a Scatter Plot of Sepal Length vs Sepal Width customized with colors by species.
    *   Create a Heatmap of the correlation matrix of all features.
    *   Plot a Histogram of Petal Length to see the distribution.
*   **Interview Questions:**
    *   When would you use a Box Plot? (Outlier detection)
    *   Scatter plot vs Line plot uses? (Correlation vs Trend over time)
    *   What is a Histogram? (Frequency distribution)
""",
            'order': 1
        },
        {
            'title': 'Linear Regression',
            'content': """# Predicting Values (Regression)

*   **One-line Explanation:** Identifying the linear relationship between input variables and a continuous output.
*   **Skills Learned:** Model fitting, understanding weights/bias, making predictions.
*   **Required Data:** **Boston Housing** or **Real Estate Price Prediction** (Columns: Sqft, Rooms -> Price). Source: Kaggle.
*   **Tools/Libraries:** Scikit-Learn.
*   **Hands-On Tasks:**
    *   Split the dataset into Training (80%) and Testing (20%) sets.
    *   Train a LinearRegression model to predict house price based on square footage.
    *   Plot the "Line of Best Fit" over the scatter plot of actual data.
*   **Interview Questions:**
    *   What is the Cost Function in Linear Regression? (MSE - Mean Squared Error)
    *   Explain Overfitting vs Underfitting. (Memorizing noise vs too simple)
    *   What is the purpose of splitting data into Train/Test? (Validation on unseen data)
""",
            'order': 2
        },
        {
            'title': 'Logistic Regression',
            'content': """# Predicting Categories (Classification)

*   **One-line Explanation:** Predicting a binary outcome (Yes/No, Spam/Not Spam).
*   **Skills Learned:** Binary classification, probability thresholds, accuracy metrics.
*   **Required Data:** **Diabetes Dataset** (Glucose, BMI -> Has Diabetes?). Source: Pima Indians Diabetes (Kaggle).
*   **Tools/Libraries:** Scikit-Learn.
*   **Hands-On Tasks:**
    *   Train a Logistic Regression model to predict diabetes presence.
    *   Calculate the Accuracy Score of the model on test data.
    *   Print the Confusion Matrix to see True Positives vs False Positives.
*   **Interview Questions:**
    *   Why not use Linear Regression for classification? (Output is unbounded, need 0-1 prob)
    *   What is the Sigmoid function? (Maps input to 0-1 range)
    *   What is a False Positive? (Model predicted Yes, but actually No)
""",
            'order': 3
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: INTERMEDIATE - Advanced ML
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Intermediate: Advanced ML Algorithms',
        description='Robust models and unsupervised learning.',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'Decision Trees & Random Forests',
            'content': """# Ensemble Learning (8-12 Weeks Stage Estimate)

*   **One-line Explanation:** Tree-based models that split data based on features to make decisions.
*   **Skills Learned:** Handling non-linear data, preventing overfitting with ensembles.
*   **Required Data:** **Wine Quality Dataset** (Acidity, Sugar -> Quality 0-10). Source: UCI.
*   **Tools/Libraries:** Scikit-Learn.
*   **Hands-On Tasks:**
    *   Train a single Decision Tree Classifier and visualize the tree structure.
    *   Train a Random Forest Classifier (100 trees) and compare accuracy with the single tree.
    *   Identify "Feature Importance" to see which chemical property affects wine quality most.
*   **Interview Questions:**
    *   What is Entropy/Gini Impurity? (Metrics to measure split quality)
    *   Why are Random Forests better than Decision Trees? (Reduce variance/overfitting)
    *   What is Bagging? (Bootstrap Aggregating - parallel training)
""",
            'order': 1
        },
        {
            'title': 'Clustering (Unsupervised)',
            'content': """# Finding Patterns (K-Means)

*   **One-line Explanation:** Grouping similar data points together without labels.
*   **Skills Learned:** Unsupervised learning, finding hidden structures.
*   **Required Data:** **Mall Customers Dataset** (Annual Income, Spending Score). Source: Kaggle.
*   **Tools/Libraries:** Scikit-Learn.
*   **Hands-On Tasks:**
    *   Apply K-Means clustering to group customers into 5 segments.
    *   Visualize the clusters using a scatter plot with different colors.
    *   Use the "Elbow Method" to find the optimal number of clusters (K).
*   **Interview Questions:**
    *   What is the difference between Supervised and Unsupervised Learning? (Labels vs No Labels)
    *   How does K-Means work? (Iteratively assigns points to nearest centroid)
    *   What is the K in K-Means? (Number of clusters)
""",
            'order': 2
        },
        {
            'title': 'Model Evaluation & Metrics',
            'content': """# How Good is the Model?

*   **One-line Explanation:** Using advanced metrics beyond just 'Accuracy' to judge performance.
*   **Skills Learned:** Precision, Recall, F1-Score, Cross-Validation.
*   **Required Data:** **Credit Card Fraud Detection** (Imbalanced Data). Source: Kaggle (use subset if large).
*   **Tools/Libraries:** Scikit-Learn.
*   **Hands-On Tasks:**
    *   Calculate Precision and Recall for a fraud detection model.
    *   Plot the ROC Curve and calculate AUC (Area Under Curve).
    *   Perform K-Fold Cross-Validation to test model stability.
*   **Interview Questions:**
    *   Why is Accuracy bad for imbalanced datasets? (99% non-fraud means 99% accuracy is easy but useless)
    *   What is Recall? (Ability to find all positive samples)
    *   Explain the Bias-Variance Tradeoff. (Simple vs Complex models)
""",
            'order': 3
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: ADVANCED - Deep Learning
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Advanced: Deep Learning',
        description='Neural Networks for Vision and Text.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'Intro to Neural Networks',
            'content': """# The Artificial Brain (10-14 Weeks Stage Estimate)

*   **One-line Explanation:** Layers of interconnected nodes (neurons) that learn complex patterns.
*   **Skills Learned:** Backpropagation, Activation Functions, PyTorch/TensorFlow basics.
*   **Required Data:** **MNIST Digit Dataset** (28x28 grayscale images of numbers). Source: Keras/PyTorch built-in.
*   **Tools/Libraries:** PyTorch or TensorFlow (Keras).
*   **Hands-On Tasks:**
    *   Build a simple Multi-Layer Perceptron (MLP) with 1 hidden layer.
    *   Train the model to classify digits (0-9) and plot the Loss curve.
    *   Experiment with ReLU vs Sigmoid activation functions.
*   **Interview Questions:**
    *   What is an Activation Function? (Introduces non-linearity)
    *   What is Backpropagation? (Algorithm to update weights based on error)
    *   What is an Epoch? (One full pass through the training data)
""",
            'order': 1
        },
        {
            'title': 'CNNs (Computer Vision)',
            'content': """# Seeing Images (Convolutional NNs)

*   **One-line Explanation:** Neural networks specialized for processing grid-like data (Images).
*   **Skills Learned:** Convolutions, Pooling, Image Classification.
*   **Required Data:** **CIFAR-10** (Color images: car, dog, plane, etc.). Source: Keras/PyTorch built-in.
*   **Tools/Libraries:** TensorFlow/Keras or PyTorch.
*   **Hands-On Tasks:**
    *   Build a CNN with Conv2D and MaxPooling layers.
    *   Train it to classify CIFAR-10 images.
    *   Use Data Augmentation (rotation, zoom) to improve accuracy.
*   **Interview Questions:**
    *   What does a Convolution layer do? (Extracts features/edges)
    *   What is Max Pooling? (Downsamples dimensions, keeps important features)
    *   Why use CNNs over MLPs for images? (Spatial invariance, fewer parameters)
""",
            'order': 2
        },
        {
            'title': 'NLP Basics (RNNs & Transformers)',
            'content': """# Understanding Text

*   **One-line Explanation:** Processing sequences of text for sentiment or translation.
*   **Skills Learned:** Tokenization, Embeddings, RNNs/LSTMs.
*   **Required Data:** **IMDB Movie Reviews** (Text -> Sentiment Pos/Neg). Source: Kaggle/Keras.
*   **Tools/Libraries:** TensorFlow/PyTorch, Hugging Face.
*   **Hands-On Tasks:**
    *   Preprocess text: Tokenize and pad sequences.
    *   Train a simple LSTM network to predict sentiment.
    *   (Bonus) Use a pre-trained BERT model from Hugging Face to classify text.
*   **Interview Questions:**
    *   What is Tokenization? (Splitting text into numbers/words)
    *   Why use RNNs for text? (Handles sequential data/variable length)
    *   What is a Word Embedding? (Vector representation of word meaning)
""",
            'order': 3
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")


    # ==========================================
    # STAGE 5: INDUSTRY-READY - Deployment
    # ==========================================
    stage5 = Stage.objects.create(
        roadmap=roadmap,
        title='Industry-Ready: Deployment',
        description='Productionizing Models.',
        order=5,
        is_free=False
    )
    
    topics_s5 = [
        {
            'title': 'Model Serialization',
            'content': """# Saving the Brain (3-6 Months Stage Estimate)

*   **One-line Explanation:** Saving a trained model to a file so it can be reloaded later.
*   **Skills Learned:** Pickle, Joblib, ONNX.
*   **Required Data:** (Use model trained in previous stages).
*   **Tools/Libraries:** Joblib, Pickle.
*   **Hands-On Tasks:**
    *   Train a Random Forest model on Iris data.
    *   Save it to a file using `joblib.dump('model.pkl')`.
    *   Load it in a separate Python script and make a prediction.
*   **Interview Questions:**
    *   Why do we need to serialize models? (To deploy without retraining)
    *   Pickle vs Joblib? (Joblib is better for large NumPy arrays)
    *   What is ONNX? (Open standard for model interoperability)
""",
            'order': 1
        },
        {
            'title': 'API Serving with FastAPI',
            'content': """# Model as a Service

*   **One-line Explanation:** Wrapping the model in a Web API so apps can talk to it.
*   **Skills Learned:** REST APIs, Request/Response handling.
*   **Required Data:** None (Input comes from API user).
*   **Tools/Libraries:** FastAPI, Uvicorn.
*   **Hands-On Tasks:**
    *   Create a FastAPI app with a `/predict` endpoint.
    *   Load the saved model on app startup.
    *   Accept JSON input (e.g., Iris measurements) and return the prediction.
*   **Interview Questions:**
    *   What is FastAPI? (High-performance Python web framework)
    *   POST vs GET for model inference? (POST is safer for data payloads)
    *   What is Swagger UI? (Auto-generated API documentation)
""",
            'order': 2
        },
        {
            'title': 'Containerization (Docker)',
            'content': """# Shipping It

*   **One-line Explanation:** Packaging code + dependencies so it runs anywhere.
*   **Skills Learned:** Dockerfiles, Building Images, Running Containers.
*   **Required Data:** None.
*   **Tools/Libraries:** Docker.
*   **Hands-On Tasks:**
    *   Write a `Dockerfile` for the FastAPI app.
    *   Build the Docker Image (`docker build`).
    *   Run the container and test the API endpoint.
*   **Interview Questions:**
    *   What is a Docker Container? (Isolated runtime environment)
    *   Dockerfile vs Image vs Container? (Recipe -> Cake Mold -> Cake)
    *   Why use Docker for ML? (Solves "it works on my machine" dependency hell)
""",
            'order': 3
        }
    ]
    
    for t in topics_s5:
        Topic.objects.create(stage=stage5, **t)
    print(f"   ✨ Added {len(topics_s5)} topics to Stage 5")

    # Update stats
    roadmap.update_stats()
    print("✅ Python for AI Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_python_ai_roadmap()
