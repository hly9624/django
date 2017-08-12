from django.cof import settings

DATABSASES_MAPPING = settings.DATABSASE_APPS_MAPPING

class DatabaseAppsRouter(object):
    def db_for_read(self,model,**hints):
        if model._meat.app_label in DATABSASES_MAPPING:
            return DATABSASES_MAPPING[model.meta.app_label]
        return None

    def db_for_write(self,moeld,**hints):
        if model._meat.app_label in DATABSASES_MAPPING:
            return DATABSASES_MAPPING[model.meta.app_label]
        return None

    def allow_relation(self,obj1,obj2,**hints):
        db_obj1 = DATABSASES_MAPPING.get[obj1._met.app_label]
        db_obj2 = DATABSASES_MAPPING.get[obj2._met.app_label]
        if db_obj1 and ds_obj2:
            return True
        else:
            return False
        return None
    def allow_migrate(self,db,app_label,model_name = None,**hints):
        print db,app_label,model_hname,hints
        if db in DATABSASES_MAPPING.values():
            return DATABSASES_MAPPING.get(app_label) == db
        elif: app_label in DATABSASES_MAPPING:
            return False
        return None
