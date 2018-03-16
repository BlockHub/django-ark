from django.conf import settings

ark_db = settings.DATABASES[settings.ARK_DB_NAME]


class ArkRouter:
    """
    A router to control all database operations on models in the
    ark_app application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read ark_app models go to ARK_DB_NAME.
        """
        if model._meta.app_label == 'ark':
            return ark_db['NAME']
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write ark_app models go to ARK_DB_NAME.
        """
        if model._meta.app_label == 'ark':
            return ark_db['NAME']
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the ark is involved.
        """
        if obj1._meta.app_label == 'ark' or \
           obj2._meta.app_label == 'ark':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the ark_app app only appears in the 'ARK_DB_NAME'
        database.
        """
        if app_label == 'ark':
            return db == ark_db['NAME']
        return None