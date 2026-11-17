# 🌱 CROPILOT AI V2 — AI-Powered Farmer Support System.

> A Django REST API based platform that helps farmers **detect crop diseases from a leaf photo**, **get crop growing recommendations**, **check market prices**, and **communicate with agriculture officers** — all in one place.

---

## 📌 Table of Contents

1. [Project Overview](#-project-overview)
2. [Modules at a Glance](#-modules-at-a-glance)
3. [Tech Stack](#-tech-stack)
4. [Module 1 — AI Crop Disease Detection (Main Module)](#-module-1--ai-crop-disease-detection-main-module)
5. [Module 2 — Crop Requirements Recommendation](#-module-2--crop-requirements-recommendation)
6. [Module 3 — Crop Market Prices](#-module-3--crop-market-prices)
7. [Module 4 — Farmer–Agriculture Officer Communication](#-module-4--farmeragriculture-officer-communication)
8. [API Documentation](#-api-documentation)
9. [Project Structure](#-project-structure)
10. [Installation & Setup](#-installation--setup)
11. [Future Work](#-future-work)
12. [Author](#-author)

---

## 🔎 Project Overview

Farmers often lose crops to diseases they cannot identify early, and they struggle to get quick advice, crop guidance and fair market prices. **CROPILOT** brings these needs together:

- Upload a leaf image → get the **disease, confidence, symptoms, impact and treatment**
- Enter a crop name → get the **best soil, fertilizer and climate** recommendations
- View **crop market prices**
- Send queries to and receive guidance from **agriculture officers**

---

## 🧩 Modules at a Glance

| # | Module | Django app | What it does |
|---|---|---|---|
| 1 | **AI Crop Disease Detection** ⭐ | `all_apps/ai_engine` | Deep-learning disease detection for Cocoa, Cardamom, Potato, Tomato |
| 2 | **Crop Requirements Recommendation** | `all_apps/ai_engine` | Recommends soil type, fertilizer, climate and more for any crop |
| 3 | **Crop Market Prices** | `all_apps/crop_prices` | Shows crop market prices to farmers |
| 4 | **Farmer–Officer Communication** | `all_apps/advisory` | Farmers and agriculture officers exchange advice and queries |

Also included: farmer dashboard, edit profile page, crop listing page.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.10, Django 5.2, Django REST Framework |
| Deep Learning | TensorFlow 2.21, Keras 3 (CNN, transfer learning) |
| Models | MobileNetV2, EfficientNetB0 |
| Image processing | Pillow, NumPy |
| Database | SQLite (Django ORM) |
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Model training | [Kaggle Notebooks](https://www.kaggle.com/jibintgeorge/code) |

---

## 🤖 AI Crop Disease Detection (Main Module)

📂 `all_apps/ai_engine`

The farmer selects a crop, uploads a leaf photo, and the system returns an instant diagnosis.

### How it works

```
 Farmer uploads leaf image + selects crop
                │
                ▼
      REST API: POST 127.0.0.1:8000/ai/api-disease-detect/
                │
        Image validated (serializer)
                │
          Routed by crop name
   ┌────────────┼──────────────┬──────────────┐
 Cocoa     Potato / Tomato   Cardamom
   │            │               │
   ▼            ▼               ▼
  Image preprocessing (resize to 224×224, normalization)
   │            │               │
   ▼            ▼               ▼
 MobileNetV2  MobileNetV2    EfficientNetB0
   └────────────┴───────┬───────┘
                        ▼
Predicted class → disease knowledge base from -> all_apps/ai_engine/disease_data.py
           (symptoms · impact · treatment)
                        ▼
      Report saved to DB → result page shown (disease_result.html)
```

### Key design points

- **Models load once at server start.** The three trained `.h5` models and `tensorflow` & `keras` are loaded into memory when Django starts (`apps.py`), so every request reuses them and predictions stay fast instead of reloading a model each time (when edits/debug).
  
- **One model per crop group.** Each request is routed to the right model based on the selected crop (`views.py`).
  
- **Model-specific preprocessing.** Images are resized to 224×224, converted into RGB, calculated pixel intensity (image pre-processing) and prepared in `preprocess_crop_image() of utils.py`.
  
- MobileNetV2 models use inputs scaled to 0–1, while EfficientNetB0 expects raw 0–255 pixels, so preprocessing is handled per model.
  
- **Rich results, not just a label.** Each prediction that is like a mathematical probability, with that we calculate disease name, confidence %, inference time, symptoms, impact and treatment from a disease knowledge base (`disease_data.py`).
  
- **Reports are stored** per farmer so past detections can be reviewed.
 
- **Cross-version compatibility.** The cardamom model was trained on Kaggle with a newer Keras than the local setup, so the loader includes a small compatibility patch for it.

### Deep learning models

| Crop | Architecture | Input | Classes |
|---|---|---|---|
| Cocoa | MobileNetV2 (transfer learning) | 224×224×3 | _(add your cocoa classes)_ |
| Potato & Tomato | MobileNetV2 (transfer learning) | 224×224×3 | _(add your potato/tomato classes)_ |
| Cardamom | **EfficientNetB0** (transfer learning) | 224×224×3 | `Blight`, `Healthy`, `LeafSpot` |

#### Cardamom model — training summary

- **Dataset:** [Kerala Cardamom Intelligence Dataset (KCID)](https://www.kaggle.com/datasets/noahjos/kerala-cardamom-intelligence-dataset-kcid)
- **Base model:** EfficientNetB0 pre-trained on ImageNet (frozen feature extractor)
- **Classifier head:** Global Average Pooling → Dropout (0.3) → Dense (3, softmax)
- **Augmentation:** random flip, rotation, zoom and contrast
- **Training:** Adam optimizer, categorical cross-entropy, 80/20 train/validation split, 12 epochs
- **Platform:** Kaggle (TensorFlow 2.21, Keras 3.13.2)

---

## 🌾 Module 2 — Crop Requirements Recommendation

📂 `all_apps/ai_engine`

The farmer types in any crop name and the system returns its growing requirements, such as:

- 🪨 **Best soil type**
- 🧪 **Recommended fertilizer**
- 🌦️ **Suitable climate** (temperature, rainfall, season)
- _(add any other fields your module returns, e.g. water needs, pH, sowing season)_

This helps farmers plan before sowing and complements disease detection once the crop is growing.

---

## 💹 Module 3 — Crop Market Prices

📂 `all_apps/crop_prices`

Farmers can view current crop market prices so they can decide when and where to sell.

- _(describe your data source, e.g. admin-updated prices or an external feed)_
- _(describe what users can see, e.g. crop-wise price list, filter by crop or date)_

---

## 💬 Module 4 — Farmer–Agriculture Officer Communication

📂 `all_apps/advisory`

A direct channel between farmers and agriculture officers:

- Farmers can **send queries** about crop problems, practices or schemes
- Agriculture officers can **view and respond** with expert advice
- Conversations are stored so advice can be revisited

_(adjust to match your implementation, e.g. message threads, status tracking, attachments)_

---

## 📡 API Documentation

**Base URL (local):** `http://127.0.0.1:8000`

### Endpoints overview

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `GET` | `/homepage/` | Home page | — |
| `GET` | `/disease_detection/` | Disease detection upload page | Logged-in farmer |
| `POST` | `/ai/api-disease-detect/` | **Detect crop disease from a leaf image** | Logged-in farmer |
| _…_ | _(add crop recommendation URL)_ | Crop requirements recommendation | _(auth)_ |
| _…_ | _(add crop prices URL)_ | Crop market prices | _(auth)_ |
| _…_ | _(add advisory URL)_ | Farmer–officer communication | _(auth)_ |

> Fill in the remaining rows from your `urls.py` files.

---

### 🔬 `POST /ai/api-disease-detect/`

Runs the AI model for the selected crop and returns the disease analysis.

**Content-Type:** `multipart/form-data`

#### Request parameters

| Field | Type | Required | Description |
|---|---|---|---|
| `image` | file (JPG / PNG) | ✅ | Leaf image of the crop |
| `crop_name` | string | ✅ | One of: `cocoa`, `cardamom`, `potato`, `tomato` |

#### Crop → model routing

| `crop_name` | Model used |
|---|---|
| `cocoa` | Cocoa MobileNetV2 |
| `potato`, `tomato` | Potato/Tomato MobileNetV2 |
| `cardamom` | Cardamom EfficientNetB0 |

#### Example request (cURL)

```bash
curl -X POST http://127.0.0.1:8000/ai/api-disease-detect/ \
  -H "Cookie: sessionid=<your-session-id>; csrftoken=<token>" \
  -H "X-CSRFToken: <token>" \
  -F "crop_name=cardamom" \
  -F "image=@/path/to/leaf.jpg"
```

#### Prediction data returned for each request

```json
{
  "disease": "Leaf Spot",
  "confidence": 94.32,
  "model_time": 0.412,
  "treatment": "Spray recommended fungicide ...",
  "impact": "Reduces photosynthesis and yield ...",
  "symptoms": "Brown spots with yellow halo on leaves ..."
}
```

| Field | Type | Description |
|---|---|---|
| `disease` | string | Predicted disease class |
| `confidence` | float | Model confidence in % |
| `model_time` | float | Inference time in seconds |
| `treatment` | string | Recommended treatment |
| `impact` | string | Effect on the crop |
| `symptoms` | string | Visible symptoms |

> The endpoint currently renders these fields into the result page as HTML. The JSON above shows the data available to the page.

#### Responses

| Status | Meaning |
|---|---|
| `200 OK` | Result page rendered with predictions |
| `200 OK` (error message) | Model failed internally — page shows an "AI Model is Not Working" message |
| `400 Bad Request` | Missing, empty or corrupted image (serializer errors returned as JSON) |
| `403 Forbidden` | Not logged in / missing CSRF token |

---

## 📁 Project Structure

```
CROPILOT_AI_V2/
├── cropilot_project/            # Django project settings & root URLs
├── all_apps/
│   ├── ai_engine/               # Disease detection + crop recommendation
│   │   ├── apps.py              # Loads ML models into memory at startup
│   │   ├── utils.py             # Image preprocessing + prediction
│   │   ├── views.py             # REST API views
│   │   ├── disease_data.py      # Class names, symptoms, impact, treatments
│   │   └── ml_models/           # Trained .h5 models (cocoa, potato/tomato, cardamom)
│   ├── advisory/                # Farmer–officer communication
│   └── crop_prices/             # Crop market prices
├── templates/                   # HTML templates
├── static/                      # CSS, JS, images
├── manage.py
└── requirements.txt
```

> Adjust to match your repository.

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/jibintgeorgecareer-DEV/CROPILOT_AI_V2.git
cd CROPILOT_AI_V2

# 2. Create and activate a virtual environment
python -m venv .my_env
.my_env\Scripts\activate          # Windows
# source .my_env/bin/activate     # Linux / macOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create an admin user
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```

Open **http://127.0.0.1:8000/homepage/**

> ⚠️ Models load only when Django runs with its auto-reloader (`runserver`). If you use `--noreload` or a production server, adjust the model-loading check in `apps.py`.

> ℹ️ Place the three `.h5` model files in `all_apps/ai_engine/ml_models/`.

---

## 🚧 Future Work

- Return a pure JSON response for mobile / third-party clients
- Token (JWT) authentication for the APIs
- Swagger / OpenAPI documentation
- More crops and diseases
- Fine-tune the cardamom model and balance classes
- Docker + gunicorn deployment

---

## 👨‍💻 Author

**Jibin T George** — BCA 2026, St. Joseph's Academy of Higher Education & Research (MGU Kottayam), Kerala, India

- GitHub: [@jibintgeorgecareer-DEV](https://github.com/jibintgeorgecareer-DEV)

⭐ If you find this project interesting, feel free to star the repository!
