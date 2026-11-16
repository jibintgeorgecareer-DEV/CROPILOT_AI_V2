import os
from django.apps import AppConfig
from django.conf import settings

class AiEngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'all_apps.ai_engine'

    COCOA_MODEL = None
    POTATO_TOMATO_MODEL = None
    CARDAMOM_MODEL = None

# -------------------- Loading ML Model into RAM when Django starts --------------------------------

    def ready(self):  # ready() is build-in django method executes all_apps.ai_engine LOADED

        if os.environ.get('RUN_MAIN') == 'true':  # Stops Django auto-reloader (explanation TOPDOWN)
            print("---------LOADING MODELS: [COCOA | CARDAMOM | POTATO | TOMATO]----------")

            from tensorflow.keras.models import load_model  #Loading heavy tensorflow & keras into RAM
            from tensorflow.keras.layers import Dense

            # Loading Cocoa .h5 model (Locating .h5 models)
            cocoa_model_path = os.path.join(
                settings.BASE_DIR, 'all_apps', 'ai_engine', 'ml_models', 'cocoa_disease_model.h5'
            )

            # Loading Potato_Tomato .h5 model
            potato_tomato_model_path = os.path.join(
                settings.BASE_DIR, 'all_apps', 'ai_engine', 'ml_models', 'plant_disease_model.h5'
            )

            # Loading Cardamom .h5 model trained on EfficientNetB0
            cardamom_model_path = os.path.join(
                settings.BASE_DIR, 'all_apps', 'ai_engine', 'ml_models', 'cardamom_disease_model.h5'
            )

            for name in ("CARDAMOM_MODEL", "COCOA_MODEL", "POTATO_TOMATO_MODEL"):
                print(name, "->", getattr(AiEngineConfig, name))

            try:                                    # Loading models into RAM

                # Reads binary .h5 from HDD load into RAM 
                AiEngineConfig.COCOA_MODEL = load_model(cocoa_model_path)
                AiEngineConfig.POTATO_TOMATO_MODEL = load_model(potato_tomato_model_path)

# ++++++++++++++++++++++++      Loading CARDAMOM model        +++++++++++++++++++++++++++++
#                              Solving version missmatch
# Cardamom model was trained on Kaggle (Keras 3.13.2), but my local Keras is 3.12.4.
# Newer Keras saves `quantization_config` in Dense layers, which the older version rejects.
# PatchedDense accepts and ignores that argument so the model can load without upgrading Keras.

                class PatchedDense(Dense):
                    def __init__(self, *args, quantization_config=None, **kwargs):
                        super().__init__(*args, **kwargs)

                AiEngineConfig.CARDAMOM_MODEL = load_model(
                        cardamom_model_path,
                        custom_objects={'Dense': PatchedDense},
                        compile=False,
                )
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                print(".h5 models Loaded into RAM!")

            except Exception as loading_error:
                print(f"ERROR -> Failed to load Model :{loading_error}")


# when python manage.py runserver: Django runs two process one for code changes another for 
# server hosting.

# when if os.environ.get('RUN_MAIN') == 'true': Django dont need to load tensorflow, model load
# twice into RAM