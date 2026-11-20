class ReadRouter_ras:
    route_app_labels = {"system_ras"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "system_ras_db"
        return None
