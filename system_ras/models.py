# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class B1SigstateChange(models.Model):
    id_item = models.AutoField(db_column='ID_ITEM', primary_key=True)  # Field name made lowercase.
    sig_name = models.CharField(db_column='SIG_NAME', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    sig_state = models.IntegerField(db_column='SIG_STATE', blank=True, null=True)  # Field name made lowercase.
    timepoint = models.DateTimeField(db_column='TIMEPOINT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'B1_SIGSTATE_CHANGE'


class B2SigstateChange(models.Model):
    id_item = models.AutoField(db_column='ID_ITEM', primary_key=True)  # Field name made lowercase.
    sig_name = models.CharField(db_column='SIG_NAME', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    sig_state = models.IntegerField(db_column='SIG_STATE', blank=True, null=True)  # Field name made lowercase.
    timepoint = models.DateTimeField(db_column='TIMEPOINT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'B2_SIGSTATE_CHANGE'


class B3SigstateChange(models.Model):
    id_item = models.AutoField(db_column='ID_ITEM', primary_key=True)  # Field name made lowercase.
    sig_name = models.CharField(db_column='SIG_NAME', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    sig_state = models.IntegerField(db_column='SIG_STATE', blank=True, null=True)  # Field name made lowercase.
    timepoint = models.DateTimeField(db_column='TIMEPOINT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'B3_SIGSTATE_CHANGE'


class L110KvaB1(models.Model):
    id_item = models.AutoField(db_column='ID_ITEM', primary_key=True)  # Field name made lowercase.
    timepoint = models.DateTimeField(db_column='TIMEPOINT', blank=True, null=True)  # Field name made lowercase.
    va000 = models.IntegerField(db_column='VA000', blank=True, null=True)  # Field name made lowercase.
    va001 = models.IntegerField(db_column='VA001', blank=True, null=True)  # Field name made lowercase.
    va002 = models.IntegerField(db_column='VA002', blank=True, null=True)  # Field name made lowercase.
    va003 = models.IntegerField(db_column='VA003', blank=True, null=True)  # Field name made lowercase.
    va004 = models.IntegerField(db_column='VA004', blank=True, null=True)  # Field name made lowercase.
    va005 = models.IntegerField(db_column='VA005', blank=True, null=True)  # Field name made lowercase.
    va006 = models.IntegerField(db_column='VA006', blank=True, null=True)  # Field name made lowercase.
    va007 = models.IntegerField(db_column='VA007', blank=True, null=True)  # Field name made lowercase.
    va010 = models.IntegerField(db_column='VA010', blank=True, null=True)  # Field name made lowercase.
    va011 = models.IntegerField(db_column='VA011', blank=True, null=True)  # Field name made lowercase.
    va012 = models.IntegerField(db_column='VA012', blank=True, null=True)  # Field name made lowercase.
    va013 = models.IntegerField(db_column='VA013', blank=True, null=True)  # Field name made lowercase.
    va014 = models.IntegerField(db_column='VA014', blank=True, null=True)  # Field name made lowercase.
    va015 = models.IntegerField(db_column='VA015', blank=True, null=True)  # Field name made lowercase.
    va016 = models.IntegerField(db_column='VA016', blank=True, null=True)  # Field name made lowercase.
    va017 = models.IntegerField(db_column='VA017', blank=True, null=True)  # Field name made lowercase.
    va020 = models.IntegerField(db_column='VA020', blank=True, null=True)  # Field name made lowercase.
    va021 = models.IntegerField(db_column='VA021', blank=True, null=True)  # Field name made lowercase.
    va022 = models.IntegerField(db_column='VA022', blank=True, null=True)  # Field name made lowercase.
    va023 = models.IntegerField(db_column='VA023', blank=True, null=True)  # Field name made lowercase.
    va024 = models.IntegerField(db_column='VA024', blank=True, null=True)  # Field name made lowercase.
    va025 = models.IntegerField(db_column='VA025', blank=True, null=True)  # Field name made lowercase.
    va026 = models.IntegerField(db_column='VA026', blank=True, null=True)  # Field name made lowercase.
    va027 = models.IntegerField(db_column='VA027', blank=True, null=True)  # Field name made lowercase.
    va030 = models.IntegerField(db_column='VA030', blank=True, null=True)  # Field name made lowercase.
    va031 = models.IntegerField(db_column='VA031', blank=True, null=True)  # Field name made lowercase.
    va032 = models.IntegerField(db_column='VA032', blank=True, null=True)  # Field name made lowercase.
    va033 = models.IntegerField(db_column='VA033', blank=True, null=True)  # Field name made lowercase.
    va034 = models.IntegerField(db_column='VA034', blank=True, null=True)  # Field name made lowercase.
    va035 = models.IntegerField(db_column='VA035', blank=True, null=True)  # Field name made lowercase.
    va036 = models.IntegerField(db_column='VA036', blank=True, null=True)  # Field name made lowercase.
    va037 = models.IntegerField(db_column='VA037', blank=True, null=True)  # Field name made lowercase.
    va040 = models.IntegerField(db_column='VA040', blank=True, null=True)  # Field name made lowercase.
    va041 = models.IntegerField(db_column='VA041', blank=True, null=True)  # Field name made lowercase.
    va042 = models.IntegerField(db_column='VA042', blank=True, null=True)  # Field name made lowercase.
    va043 = models.IntegerField(db_column='VA043', blank=True, null=True)  # Field name made lowercase.
    va044 = models.IntegerField(db_column='VA044', blank=True, null=True)  # Field name made lowercase.
    va045 = models.IntegerField(db_column='VA045', blank=True, null=True)  # Field name made lowercase.
    va046 = models.IntegerField(db_column='VA046', blank=True, null=True)  # Field name made lowercase.
    va047 = models.IntegerField(db_column='VA047', blank=True, null=True)  # Field name made lowercase.
    va050 = models.IntegerField(db_column='VA050', blank=True, null=True)  # Field name made lowercase.
    va051 = models.IntegerField(db_column='VA051', blank=True, null=True)  # Field name made lowercase.
    va052 = models.IntegerField(db_column='VA052', blank=True, null=True)  # Field name made lowercase.
    va053 = models.IntegerField(db_column='VA053', blank=True, null=True)  # Field name made lowercase.
    va054 = models.IntegerField(db_column='VA054', blank=True, null=True)  # Field name made lowercase.
    va055 = models.IntegerField(db_column='VA055', blank=True, null=True)  # Field name made lowercase.
    va056 = models.IntegerField(db_column='VA056', blank=True, null=True)  # Field name made lowercase.
    va057 = models.IntegerField(db_column='VA057', blank=True, null=True)  # Field name made lowercase.
    va060 = models.IntegerField(db_column='VA060', blank=True, null=True)  # Field name made lowercase.
    va061 = models.IntegerField(db_column='VA061', blank=True, null=True)  # Field name made lowercase.
    va062 = models.IntegerField(db_column='VA062', blank=True, null=True)  # Field name made lowercase.
    va063 = models.IntegerField(db_column='VA063', blank=True, null=True)  # Field name made lowercase.
    va064 = models.IntegerField(db_column='VA064', blank=True, null=True)  # Field name made lowercase.
    va065 = models.IntegerField(db_column='VA065', blank=True, null=True)  # Field name made lowercase.
    va066 = models.IntegerField(db_column='VA066', blank=True, null=True)  # Field name made lowercase.
    va067 = models.IntegerField(db_column='VA067', blank=True, null=True)  # Field name made lowercase.
    va070 = models.IntegerField(db_column='VA070', blank=True, null=True)  # Field name made lowercase.
    va071 = models.IntegerField(db_column='VA071', blank=True, null=True)  # Field name made lowercase.
    va072 = models.IntegerField(db_column='VA072', blank=True, null=True)  # Field name made lowercase.
    va073 = models.IntegerField(db_column='VA073', blank=True, null=True)  # Field name made lowercase.
    va074 = models.IntegerField(db_column='VA074', blank=True, null=True)  # Field name made lowercase.
    va075 = models.IntegerField(db_column='VA075', blank=True, null=True)  # Field name made lowercase.
    va076 = models.IntegerField(db_column='VA076', blank=True, null=True)  # Field name made lowercase.
    va077 = models.IntegerField(db_column='VA077', blank=True, null=True)  # Field name made lowercase.
    va100 = models.IntegerField(db_column='VA100', blank=True, null=True)  # Field name made lowercase.
    va101 = models.IntegerField(db_column='VA101', blank=True, null=True)  # Field name made lowercase.
    va102 = models.IntegerField(db_column='VA102', blank=True, null=True)  # Field name made lowercase.
    va103 = models.IntegerField(db_column='VA103', blank=True, null=True)  # Field name made lowercase.
    va104 = models.IntegerField(db_column='VA104', blank=True, null=True)  # Field name made lowercase.
    va105 = models.IntegerField(db_column='VA105', blank=True, null=True)  # Field name made lowercase.
    va106 = models.IntegerField(db_column='VA106', blank=True, null=True)  # Field name made lowercase.
    va107 = models.IntegerField(db_column='VA107', blank=True, null=True)  # Field name made lowercase.
    va110 = models.IntegerField(db_column='VA110', blank=True, null=True)  # Field name made lowercase.
    va111 = models.IntegerField(db_column='VA111', blank=True, null=True)  # Field name made lowercase.
    va112 = models.IntegerField(db_column='VA112', blank=True, null=True)  # Field name made lowercase.
    va113 = models.IntegerField(db_column='VA113', blank=True, null=True)  # Field name made lowercase.
    va114 = models.IntegerField(db_column='VA114', blank=True, null=True)  # Field name made lowercase.
    va115 = models.IntegerField(db_column='VA115', blank=True, null=True)  # Field name made lowercase.
    va116 = models.IntegerField(db_column='VA116', blank=True, null=True)  # Field name made lowercase.
    va117 = models.IntegerField(db_column='VA117', blank=True, null=True)  # Field name made lowercase.
    va120 = models.IntegerField(db_column='VA120', blank=True, null=True)  # Field name made lowercase.
    va121 = models.IntegerField(db_column='VA121', blank=True, null=True)  # Field name made lowercase.
    va122 = models.IntegerField(db_column='VA122', blank=True, null=True)  # Field name made lowercase.
    va123 = models.IntegerField(db_column='VA123', blank=True, null=True)  # Field name made lowercase.
    va124 = models.IntegerField(db_column='VA124', blank=True, null=True)  # Field name made lowercase.
    va125 = models.IntegerField(db_column='VA125', blank=True, null=True)  # Field name made lowercase.
    va126 = models.IntegerField(db_column='VA126', blank=True, null=True)  # Field name made lowercase.
    va127 = models.IntegerField(db_column='VA127', blank=True, null=True)  # Field name made lowercase.
    va130 = models.IntegerField(db_column='VA130', blank=True, null=True)  # Field name made lowercase.
    va131 = models.IntegerField(db_column='VA131', blank=True, null=True)  # Field name made lowercase.
    va132 = models.IntegerField(db_column='VA132', blank=True, null=True)  # Field name made lowercase.
    va133 = models.IntegerField(db_column='VA133', blank=True, null=True)  # Field name made lowercase.
    va134 = models.IntegerField(db_column='VA134', blank=True, null=True)  # Field name made lowercase.
    va135 = models.IntegerField(db_column='VA135', blank=True, null=True)  # Field name made lowercase.
    va136 = models.IntegerField(db_column='VA136', blank=True, null=True)  # Field name made lowercase.
    va137 = models.IntegerField(db_column='VA137', blank=True, null=True)  # Field name made lowercase.
    va140 = models.IntegerField(db_column='VA140', blank=True, null=True)  # Field name made lowercase.
    va141 = models.IntegerField(db_column='VA141', blank=True, null=True)  # Field name made lowercase.
    va142 = models.IntegerField(db_column='VA142', blank=True, null=True)  # Field name made lowercase.
    va143 = models.IntegerField(db_column='VA143', blank=True, null=True)  # Field name made lowercase.
    va144 = models.IntegerField(db_column='VA144', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'L110KVA_B1'


class L110KvaB2(models.Model):
    id_item = models.AutoField(db_column='ID_ITEM', primary_key=True)  # Field name made lowercase.
    timepoint = models.DateTimeField(db_column='TIMEPOINT', blank=True, null=True)  # Field name made lowercase.
    va000 = models.IntegerField(db_column='VA000', blank=True, null=True)  # Field name made lowercase.
    va001 = models.IntegerField(db_column='VA001', blank=True, null=True)  # Field name made lowercase.
    va002 = models.IntegerField(db_column='VA002', blank=True, null=True)  # Field name made lowercase.
    va003 = models.IntegerField(db_column='VA003', blank=True, null=True)  # Field name made lowercase.
    va004 = models.IntegerField(db_column='VA004', blank=True, null=True)  # Field name made lowercase.
    va005 = models.IntegerField(db_column='VA005', blank=True, null=True)  # Field name made lowercase.
    va006 = models.IntegerField(db_column='VA006', blank=True, null=True)  # Field name made lowercase.
    va007 = models.IntegerField(db_column='VA007', blank=True, null=True)  # Field name made lowercase.
    va010 = models.IntegerField(db_column='VA010', blank=True, null=True)  # Field name made lowercase.
    va011 = models.IntegerField(db_column='VA011', blank=True, null=True)  # Field name made lowercase.
    va012 = models.IntegerField(db_column='VA012', blank=True, null=True)  # Field name made lowercase.
    va013 = models.IntegerField(db_column='VA013', blank=True, null=True)  # Field name made lowercase.
    va014 = models.IntegerField(db_column='VA014', blank=True, null=True)  # Field name made lowercase.
    va015 = models.IntegerField(db_column='VA015', blank=True, null=True)  # Field name made lowercase.
    va016 = models.IntegerField(db_column='VA016', blank=True, null=True)  # Field name made lowercase.
    va017 = models.IntegerField(db_column='VA017', blank=True, null=True)  # Field name made lowercase.
    va020 = models.IntegerField(db_column='VA020', blank=True, null=True)  # Field name made lowercase.
    va021 = models.IntegerField(db_column='VA021', blank=True, null=True)  # Field name made lowercase.
    va022 = models.IntegerField(db_column='VA022', blank=True, null=True)  # Field name made lowercase.
    va023 = models.IntegerField(db_column='VA023', blank=True, null=True)  # Field name made lowercase.
    va024 = models.IntegerField(db_column='VA024', blank=True, null=True)  # Field name made lowercase.
    va025 = models.IntegerField(db_column='VA025', blank=True, null=True)  # Field name made lowercase.
    va026 = models.IntegerField(db_column='VA026', blank=True, null=True)  # Field name made lowercase.
    va027 = models.IntegerField(db_column='VA027', blank=True, null=True)  # Field name made lowercase.
    va030 = models.IntegerField(db_column='VA030', blank=True, null=True)  # Field name made lowercase.
    va031 = models.IntegerField(db_column='VA031', blank=True, null=True)  # Field name made lowercase.
    va032 = models.IntegerField(db_column='VA032', blank=True, null=True)  # Field name made lowercase.
    va033 = models.IntegerField(db_column='VA033', blank=True, null=True)  # Field name made lowercase.
    va034 = models.IntegerField(db_column='VA034', blank=True, null=True)  # Field name made lowercase.
    va035 = models.IntegerField(db_column='VA035', blank=True, null=True)  # Field name made lowercase.
    va036 = models.IntegerField(db_column='VA036', blank=True, null=True)  # Field name made lowercase.
    va037 = models.IntegerField(db_column='VA037', blank=True, null=True)  # Field name made lowercase.
    va040 = models.IntegerField(db_column='VA040', blank=True, null=True)  # Field name made lowercase.
    va041 = models.IntegerField(db_column='VA041', blank=True, null=True)  # Field name made lowercase.
    va042 = models.IntegerField(db_column='VA042', blank=True, null=True)  # Field name made lowercase.
    va043 = models.IntegerField(db_column='VA043', blank=True, null=True)  # Field name made lowercase.
    va044 = models.IntegerField(db_column='VA044', blank=True, null=True)  # Field name made lowercase.
    va045 = models.IntegerField(db_column='VA045', blank=True, null=True)  # Field name made lowercase.
    va046 = models.IntegerField(db_column='VA046', blank=True, null=True)  # Field name made lowercase.
    va047 = models.IntegerField(db_column='VA047', blank=True, null=True)  # Field name made lowercase.
    va050 = models.IntegerField(db_column='VA050', blank=True, null=True)  # Field name made lowercase.
    va051 = models.IntegerField(db_column='VA051', blank=True, null=True)  # Field name made lowercase.
    va052 = models.IntegerField(db_column='VA052', blank=True, null=True)  # Field name made lowercase.
    va053 = models.IntegerField(db_column='VA053', blank=True, null=True)  # Field name made lowercase.
    va054 = models.IntegerField(db_column='VA054', blank=True, null=True)  # Field name made lowercase.
    va055 = models.IntegerField(db_column='VA055', blank=True, null=True)  # Field name made lowercase.
    va056 = models.IntegerField(db_column='VA056', blank=True, null=True)  # Field name made lowercase.
    va057 = models.IntegerField(db_column='VA057', blank=True, null=True)  # Field name made lowercase.
    va060 = models.IntegerField(db_column='VA060', blank=True, null=True)  # Field name made lowercase.
    va061 = models.IntegerField(db_column='VA061', blank=True, null=True)  # Field name made lowercase.
    va062 = models.IntegerField(db_column='VA062', blank=True, null=True)  # Field name made lowercase.
    va063 = models.IntegerField(db_column='VA063', blank=True, null=True)  # Field name made lowercase.
    va064 = models.IntegerField(db_column='VA064', blank=True, null=True)  # Field name made lowercase.
    va065 = models.IntegerField(db_column='VA065', blank=True, null=True)  # Field name made lowercase.
    va066 = models.IntegerField(db_column='VA066', blank=True, null=True)  # Field name made lowercase.
    va067 = models.IntegerField(db_column='VA067', blank=True, null=True)  # Field name made lowercase.
    va070 = models.IntegerField(db_column='VA070', blank=True, null=True)  # Field name made lowercase.
    va071 = models.IntegerField(db_column='VA071', blank=True, null=True)  # Field name made lowercase.
    va072 = models.IntegerField(db_column='VA072', blank=True, null=True)  # Field name made lowercase.
    va073 = models.IntegerField(db_column='VA073', blank=True, null=True)  # Field name made lowercase.
    va074 = models.IntegerField(db_column='VA074', blank=True, null=True)  # Field name made lowercase.
    va075 = models.IntegerField(db_column='VA075', blank=True, null=True)  # Field name made lowercase.
    va076 = models.IntegerField(db_column='VA076', blank=True, null=True)  # Field name made lowercase.
    va077 = models.IntegerField(db_column='VA077', blank=True, null=True)  # Field name made lowercase.
    va100 = models.IntegerField(db_column='VA100', blank=True, null=True)  # Field name made lowercase.
    va101 = models.IntegerField(db_column='VA101', blank=True, null=True)  # Field name made lowercase.
    va102 = models.IntegerField(db_column='VA102', blank=True, null=True)  # Field name made lowercase.
    va103 = models.IntegerField(db_column='VA103', blank=True, null=True)  # Field name made lowercase.
    va104 = models.IntegerField(db_column='VA104', blank=True, null=True)  # Field name made lowercase.
    va105 = models.IntegerField(db_column='VA105', blank=True, null=True)  # Field name made lowercase.
    va106 = models.IntegerField(db_column='VA106', blank=True, null=True)  # Field name made lowercase.
    va107 = models.IntegerField(db_column='VA107', blank=True, null=True)  # Field name made lowercase.
    va110 = models.IntegerField(db_column='VA110', blank=True, null=True)  # Field name made lowercase.
    va111 = models.IntegerField(db_column='VA111', blank=True, null=True)  # Field name made lowercase.
    va112 = models.IntegerField(db_column='VA112', blank=True, null=True)  # Field name made lowercase.
    va113 = models.IntegerField(db_column='VA113', blank=True, null=True)  # Field name made lowercase.
    va114 = models.IntegerField(db_column='VA114', blank=True, null=True)  # Field name made lowercase.
    va115 = models.IntegerField(db_column='VA115', blank=True, null=True)  # Field name made lowercase.
    va116 = models.IntegerField(db_column='VA116', blank=True, null=True)  # Field name made lowercase.
    va117 = models.IntegerField(db_column='VA117', blank=True, null=True)  # Field name made lowercase.
    va120 = models.IntegerField(db_column='VA120', blank=True, null=True)  # Field name made lowercase.
    va121 = models.IntegerField(db_column='VA121', blank=True, null=True)  # Field name made lowercase.
    va122 = models.IntegerField(db_column='VA122', blank=True, null=True)  # Field name made lowercase.
    va123 = models.IntegerField(db_column='VA123', blank=True, null=True)  # Field name made lowercase.
    va124 = models.IntegerField(db_column='VA124', blank=True, null=True)  # Field name made lowercase.
    va125 = models.IntegerField(db_column='VA125', blank=True, null=True)  # Field name made lowercase.
    va126 = models.IntegerField(db_column='VA126', blank=True, null=True)  # Field name made lowercase.
    va127 = models.IntegerField(db_column='VA127', blank=True, null=True)  # Field name made lowercase.
    va130 = models.IntegerField(db_column='VA130', blank=True, null=True)  # Field name made lowercase.
    va131 = models.IntegerField(db_column='VA131', blank=True, null=True)  # Field name made lowercase.
    va132 = models.IntegerField(db_column='VA132', blank=True, null=True)  # Field name made lowercase.
    va133 = models.IntegerField(db_column='VA133', blank=True, null=True)  # Field name made lowercase.
    va134 = models.IntegerField(db_column='VA134', blank=True, null=True)  # Field name made lowercase.
    va135 = models.IntegerField(db_column='VA135', blank=True, null=True)  # Field name made lowercase.
    va136 = models.IntegerField(db_column='VA136', blank=True, null=True)  # Field name made lowercase.
    va137 = models.IntegerField(db_column='VA137', blank=True, null=True)  # Field name made lowercase.
    va140 = models.IntegerField(db_column='VA140', blank=True, null=True)  # Field name made lowercase.
    va141 = models.IntegerField(db_column='VA141', blank=True, null=True)  # Field name made lowercase.
    va142 = models.IntegerField(db_column='VA142', blank=True, null=True)  # Field name made lowercase.
    va143 = models.IntegerField(db_column='VA143', blank=True, null=True)  # Field name made lowercase.
    va144 = models.IntegerField(db_column='VA144', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'L110KVA_B2'


class L110KvaB3(models.Model):
    id_item = models.AutoField(db_column='ID_ITEM', primary_key=True)  # Field name made lowercase.
    timepoint = models.DateTimeField(db_column='TIMEPOINT', unique=True, blank=True,
                                     null=True)  # Field name made lowercase.
    va000 = models.IntegerField(db_column='VA000', blank=True, null=True)  # Field name made lowercase.
    va001 = models.IntegerField(db_column='VA001', blank=True, null=True)  # Field name made lowercase.
    va002 = models.IntegerField(db_column='VA002', blank=True, null=True)  # Field name made lowercase.
    va003 = models.IntegerField(db_column='VA003', blank=True, null=True)  # Field name made lowercase.
    va004 = models.IntegerField(db_column='VA004', blank=True, null=True)  # Field name made lowercase.
    va005 = models.IntegerField(db_column='VA005', blank=True, null=True)  # Field name made lowercase.
    va006 = models.IntegerField(db_column='VA006', blank=True, null=True)  # Field name made lowercase.
    va007 = models.IntegerField(db_column='VA007', blank=True, null=True)  # Field name made lowercase.
    va010 = models.IntegerField(db_column='VA010', blank=True, null=True)  # Field name made lowercase.
    va011 = models.IntegerField(db_column='VA011', blank=True, null=True)  # Field name made lowercase.
    va012 = models.IntegerField(db_column='VA012', blank=True, null=True)  # Field name made lowercase.
    va013 = models.IntegerField(db_column='VA013', blank=True, null=True)  # Field name made lowercase.
    va014 = models.IntegerField(db_column='VA014', blank=True, null=True)  # Field name made lowercase.
    va015 = models.IntegerField(db_column='VA015', blank=True, null=True)  # Field name made lowercase.
    va016 = models.IntegerField(db_column='VA016', blank=True, null=True)  # Field name made lowercase.
    va017 = models.IntegerField(db_column='VA017', blank=True, null=True)  # Field name made lowercase.
    va020 = models.IntegerField(db_column='VA020', blank=True, null=True)  # Field name made lowercase.
    va021 = models.IntegerField(db_column='VA021', blank=True, null=True)  # Field name made lowercase.
    va022 = models.IntegerField(db_column='VA022', blank=True, null=True)  # Field name made lowercase.
    va023 = models.IntegerField(db_column='VA023', blank=True, null=True)  # Field name made lowercase.
    va024 = models.IntegerField(db_column='VA024', blank=True, null=True)  # Field name made lowercase.
    va025 = models.IntegerField(db_column='VA025', blank=True, null=True)  # Field name made lowercase.
    va026 = models.IntegerField(db_column='VA026', blank=True, null=True)  # Field name made lowercase.
    va027 = models.IntegerField(db_column='VA027', blank=True, null=True)  # Field name made lowercase.
    va030 = models.IntegerField(db_column='VA030', blank=True, null=True)  # Field name made lowercase.
    va031 = models.IntegerField(db_column='VA031', blank=True, null=True)  # Field name made lowercase.
    va032 = models.IntegerField(db_column='VA032', blank=True, null=True)  # Field name made lowercase.
    va033 = models.IntegerField(db_column='VA033', blank=True, null=True)  # Field name made lowercase.
    va034 = models.IntegerField(db_column='VA034', blank=True, null=True)  # Field name made lowercase.
    va035 = models.IntegerField(db_column='VA035', blank=True, null=True)  # Field name made lowercase.
    va036 = models.IntegerField(db_column='VA036', blank=True, null=True)  # Field name made lowercase.
    va037 = models.IntegerField(db_column='VA037', blank=True, null=True)  # Field name made lowercase.
    va040 = models.IntegerField(db_column='VA040', blank=True, null=True)  # Field name made lowercase.
    va041 = models.IntegerField(db_column='VA041', blank=True, null=True)  # Field name made lowercase.
    va042 = models.IntegerField(db_column='VA042', blank=True, null=True)  # Field name made lowercase.
    va043 = models.IntegerField(db_column='VA043', blank=True, null=True)  # Field name made lowercase.
    va044 = models.IntegerField(db_column='VA044', blank=True, null=True)  # Field name made lowercase.
    va045 = models.IntegerField(db_column='VA045', blank=True, null=True)  # Field name made lowercase.
    va046 = models.IntegerField(db_column='VA046', blank=True, null=True)  # Field name made lowercase.
    va047 = models.IntegerField(db_column='VA047', blank=True, null=True)  # Field name made lowercase.
    va050 = models.IntegerField(db_column='VA050', blank=True, null=True)  # Field name made lowercase.
    va051 = models.IntegerField(db_column='VA051', blank=True, null=True)  # Field name made lowercase.
    va052 = models.IntegerField(db_column='VA052', blank=True, null=True)  # Field name made lowercase.
    va053 = models.IntegerField(db_column='VA053', blank=True, null=True)  # Field name made lowercase.
    va054 = models.IntegerField(db_column='VA054', blank=True, null=True)  # Field name made lowercase.
    va055 = models.IntegerField(db_column='VA055', blank=True, null=True)  # Field name made lowercase.
    va056 = models.IntegerField(db_column='VA056', blank=True, null=True)  # Field name made lowercase.
    va057 = models.IntegerField(db_column='VA057', blank=True, null=True)  # Field name made lowercase.
    va060 = models.IntegerField(db_column='VA060', blank=True, null=True)  # Field name made lowercase.
    va061 = models.IntegerField(db_column='VA061', blank=True, null=True)  # Field name made lowercase.
    va062 = models.IntegerField(db_column='VA062', blank=True, null=True)  # Field name made lowercase.
    va063 = models.IntegerField(db_column='VA063', blank=True, null=True)  # Field name made lowercase.
    va064 = models.IntegerField(db_column='VA064', blank=True, null=True)  # Field name made lowercase.
    va065 = models.IntegerField(db_column='VA065', blank=True, null=True)  # Field name made lowercase.
    va066 = models.IntegerField(db_column='VA066', blank=True, null=True)  # Field name made lowercase.
    va067 = models.IntegerField(db_column='VA067', blank=True, null=True)  # Field name made lowercase.
    va070 = models.IntegerField(db_column='VA070', blank=True, null=True)  # Field name made lowercase.
    va071 = models.IntegerField(db_column='VA071', blank=True, null=True)  # Field name made lowercase.
    va072 = models.IntegerField(db_column='VA072', blank=True, null=True)  # Field name made lowercase.
    va073 = models.IntegerField(db_column='VA073', blank=True, null=True)  # Field name made lowercase.
    va074 = models.IntegerField(db_column='VA074', blank=True, null=True)  # Field name made lowercase.
    va075 = models.IntegerField(db_column='VA075', blank=True, null=True)  # Field name made lowercase.
    va076 = models.IntegerField(db_column='VA076', blank=True, null=True)  # Field name made lowercase.
    va077 = models.IntegerField(db_column='VA077', blank=True, null=True)  # Field name made lowercase.
    va100 = models.IntegerField(db_column='VA100', blank=True, null=True)  # Field name made lowercase.
    va101 = models.IntegerField(db_column='VA101', blank=True, null=True)  # Field name made lowercase.
    va102 = models.IntegerField(db_column='VA102', blank=True, null=True)  # Field name made lowercase.
    va103 = models.IntegerField(db_column='VA103', blank=True, null=True)  # Field name made lowercase.
    va104 = models.IntegerField(db_column='VA104', blank=True, null=True)  # Field name made lowercase.
    va105 = models.IntegerField(db_column='VA105', blank=True, null=True)  # Field name made lowercase.
    va106 = models.IntegerField(db_column='VA106', blank=True, null=True)  # Field name made lowercase.
    va107 = models.IntegerField(db_column='VA107', blank=True, null=True)  # Field name made lowercase.
    va110 = models.IntegerField(db_column='VA110', blank=True, null=True)  # Field name made lowercase.
    va111 = models.IntegerField(db_column='VA111', blank=True, null=True)  # Field name made lowercase.
    va112 = models.IntegerField(db_column='VA112', blank=True, null=True)  # Field name made lowercase.
    va113 = models.IntegerField(db_column='VA113', blank=True, null=True)  # Field name made lowercase.
    va114 = models.IntegerField(db_column='VA114', blank=True, null=True)  # Field name made lowercase.
    va115 = models.IntegerField(db_column='VA115', blank=True, null=True)  # Field name made lowercase.
    va116 = models.IntegerField(db_column='VA116', blank=True, null=True)  # Field name made lowercase.
    va117 = models.IntegerField(db_column='VA117', blank=True, null=True)  # Field name made lowercase.
    va120 = models.IntegerField(db_column='VA120', blank=True, null=True)  # Field name made lowercase.
    va121 = models.IntegerField(db_column='VA121', blank=True, null=True)  # Field name made lowercase.
    va122 = models.IntegerField(db_column='VA122', blank=True, null=True)  # Field name made lowercase.
    va123 = models.IntegerField(db_column='VA123', blank=True, null=True)  # Field name made lowercase.
    va124 = models.IntegerField(db_column='VA124', blank=True, null=True)  # Field name made lowercase.
    va125 = models.IntegerField(db_column='VA125', blank=True, null=True)  # Field name made lowercase.
    va126 = models.IntegerField(db_column='VA126', blank=True, null=True)  # Field name made lowercase.
    va127 = models.IntegerField(db_column='VA127', blank=True, null=True)  # Field name made lowercase.
    va130 = models.IntegerField(db_column='VA130', blank=True, null=True)  # Field name made lowercase.
    va131 = models.IntegerField(db_column='VA131', blank=True, null=True)  # Field name made lowercase.
    va132 = models.IntegerField(db_column='VA132', blank=True, null=True)  # Field name made lowercase.
    va133 = models.IntegerField(db_column='VA133', blank=True, null=True)  # Field name made lowercase.
    va134 = models.IntegerField(db_column='VA134', blank=True, null=True)  # Field name made lowercase.
    va135 = models.IntegerField(db_column='VA135', blank=True, null=True)  # Field name made lowercase.
    va136 = models.IntegerField(db_column='VA136', blank=True, null=True)  # Field name made lowercase.
    va137 = models.IntegerField(db_column='VA137', blank=True, null=True)  # Field name made lowercase.
    va140 = models.IntegerField(db_column='VA140', blank=True, null=True)  # Field name made lowercase.
    va141 = models.IntegerField(db_column='VA141', blank=True, null=True)  # Field name made lowercase.
    va142 = models.IntegerField(db_column='VA142', blank=True, null=True)  # Field name made lowercase.
    va143 = models.IntegerField(db_column='VA143', blank=True, null=True)  # Field name made lowercase.
    va144 = models.IntegerField(db_column='VA144', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'L110KVA_B3'


class L110KvdB1(models.Model):
    id_item = models.AutoField(db_column='ID_ITEM', primary_key=True)  # Field name made lowercase.
    timepoint = models.DateTimeField(db_column='TIMEPOINT', unique=True, blank=True,
                                     null=True)  # Field name made lowercase.
    vd000 = models.IntegerField(db_column='VD000', blank=True, null=True)  # Field name made lowercase.
    vd001 = models.IntegerField(db_column='VD001', blank=True, null=True)  # Field name made lowercase.
    vd002 = models.IntegerField(db_column='VD002', blank=True, null=True)  # Field name made lowercase.
    vd003 = models.IntegerField(db_column='VD003', blank=True, null=True)  # Field name made lowercase.
    vd004 = models.IntegerField(db_column='VD004', blank=True, null=True)  # Field name made lowercase.
    vd005 = models.IntegerField(db_column='VD005', blank=True, null=True)  # Field name made lowercase.
    vd006 = models.IntegerField(db_column='VD006', blank=True, null=True)  # Field name made lowercase.
    vd007 = models.IntegerField(db_column='VD007', blank=True, null=True)  # Field name made lowercase.
    vd010 = models.IntegerField(db_column='VD010', blank=True, null=True)  # Field name made lowercase.
    vd011 = models.IntegerField(db_column='VD011', blank=True, null=True)  # Field name made lowercase.
    vd012 = models.IntegerField(db_column='VD012', blank=True, null=True)  # Field name made lowercase.
    vd013 = models.IntegerField(db_column='VD013', blank=True, null=True)  # Field name made lowercase.
    vd014 = models.IntegerField(db_column='VD014', blank=True, null=True)  # Field name made lowercase.
    vd015 = models.IntegerField(db_column='VD015', blank=True, null=True)  # Field name made lowercase.
    vd016 = models.IntegerField(db_column='VD016', blank=True, null=True)  # Field name made lowercase.
    vd017 = models.IntegerField(db_column='VD017', blank=True, null=True)  # Field name made lowercase.
    vd020 = models.IntegerField(db_column='VD020', blank=True, null=True)  # Field name made lowercase.
    vd021 = models.IntegerField(db_column='VD021', blank=True, null=True)  # Field name made lowercase.
    vd022 = models.IntegerField(db_column='VD022', blank=True, null=True)  # Field name made lowercase.
    vd023 = models.IntegerField(db_column='VD023', blank=True, null=True)  # Field name made lowercase.
    vd024 = models.IntegerField(db_column='VD024', blank=True, null=True)  # Field name made lowercase.
    vd025 = models.IntegerField(db_column='VD025', blank=True, null=True)  # Field name made lowercase.
    vd026 = models.IntegerField(db_column='VD026', blank=True, null=True)  # Field name made lowercase.
    vd027 = models.IntegerField(db_column='VD027', blank=True, null=True)  # Field name made lowercase.
    vd030 = models.IntegerField(db_column='VD030', blank=True, null=True)  # Field name made lowercase.
    vd031 = models.IntegerField(db_column='VD031', blank=True, null=True)  # Field name made lowercase.
    vd032 = models.IntegerField(db_column='VD032', blank=True, null=True)  # Field name made lowercase.
    vd033 = models.IntegerField(db_column='VD033', blank=True, null=True)  # Field name made lowercase.
    vd034 = models.IntegerField(db_column='VD034', blank=True, null=True)  # Field name made lowercase.
    vd035 = models.IntegerField(db_column='VD035', blank=True, null=True)  # Field name made lowercase.
    vd036 = models.IntegerField(db_column='VD036', blank=True, null=True)  # Field name made lowercase.
    vd037 = models.IntegerField(db_column='VD037', blank=True, null=True)  # Field name made lowercase.
    vd040 = models.IntegerField(db_column='VD040', blank=True, null=True)  # Field name made lowercase.
    vd041 = models.IntegerField(db_column='VD041', blank=True, null=True)  # Field name made lowercase.
    vd042 = models.IntegerField(db_column='VD042', blank=True, null=True)  # Field name made lowercase.
    vd043 = models.IntegerField(db_column='VD043', blank=True, null=True)  # Field name made lowercase.
    vd044 = models.IntegerField(db_column='VD044', blank=True, null=True)  # Field name made lowercase.
    vd045 = models.IntegerField(db_column='VD045', blank=True, null=True)  # Field name made lowercase.
    vd046 = models.IntegerField(db_column='VD046', blank=True, null=True)  # Field name made lowercase.
    vd047 = models.IntegerField(db_column='VD047', blank=True, null=True)  # Field name made lowercase.
    vd050 = models.IntegerField(db_column='VD050', blank=True, null=True)  # Field name made lowercase.
    vd051 = models.IntegerField(db_column='VD051', blank=True, null=True)  # Field name made lowercase.
    vd052 = models.IntegerField(db_column='VD052', blank=True, null=True)  # Field name made lowercase.
    vd053 = models.IntegerField(db_column='VD053', blank=True, null=True)  # Field name made lowercase.
    vd054 = models.IntegerField(db_column='VD054', blank=True, null=True)  # Field name made lowercase.
    vd055 = models.IntegerField(db_column='VD055', blank=True, null=True)  # Field name made lowercase.
    vd056 = models.IntegerField(db_column='VD056', blank=True, null=True)  # Field name made lowercase.
    vd057 = models.IntegerField(db_column='VD057', blank=True, null=True)  # Field name made lowercase.
    vd060 = models.IntegerField(db_column='VD060', blank=True, null=True)  # Field name made lowercase.
    vd061 = models.IntegerField(db_column='VD061', blank=True, null=True)  # Field name made lowercase.
    vd062 = models.IntegerField(db_column='VD062', blank=True, null=True)  # Field name made lowercase.
    vd063 = models.IntegerField(db_column='VD063', blank=True, null=True)  # Field name made lowercase.
    vd064 = models.IntegerField(db_column='VD064', blank=True, null=True)  # Field name made lowercase.
    vd065 = models.IntegerField(db_column='VD065', blank=True, null=True)  # Field name made lowercase.
    vd066 = models.IntegerField(db_column='VD066', blank=True, null=True)  # Field name made lowercase.
    vd067 = models.IntegerField(db_column='VD067', blank=True, null=True)  # Field name made lowercase.
    vd070 = models.IntegerField(db_column='VD070', blank=True, null=True)  # Field name made lowercase.
    vd071 = models.IntegerField(db_column='VD071', blank=True, null=True)  # Field name made lowercase.
    vd072 = models.IntegerField(db_column='VD072', blank=True, null=True)  # Field name made lowercase.
    vd073 = models.IntegerField(db_column='VD073', blank=True, null=True)  # Field name made lowercase.
    vd074 = models.IntegerField(db_column='VD074', blank=True, null=True)  # Field name made lowercase.
    vd075 = models.IntegerField(db_column='VD075', blank=True, null=True)  # Field name made lowercase.
    vd076 = models.IntegerField(db_column='VD076', blank=True, null=True)  # Field name made lowercase.
    vd077 = models.IntegerField(db_column='VD077', blank=True, null=True)  # Field name made lowercase.
    vd100 = models.IntegerField(db_column='VD100', blank=True, null=True)  # Field name made lowercase.
    vd101 = models.IntegerField(db_column='VD101', blank=True, null=True)  # Field name made lowercase.
    vd102 = models.IntegerField(db_column='VD102', blank=True, null=True)  # Field name made lowercase.
    vd103 = models.IntegerField(db_column='VD103', blank=True, null=True)  # Field name made lowercase.
    vd104 = models.IntegerField(db_column='VD104', blank=True, null=True)  # Field name made lowercase.
    vd105 = models.IntegerField(db_column='VD105', blank=True, null=True)  # Field name made lowercase.
    vd106 = models.IntegerField(db_column='VD106', blank=True, null=True)  # Field name made lowercase.
    vd107 = models.IntegerField(db_column='VD107', blank=True, null=True)  # Field name made lowercase.
    vd110 = models.IntegerField(db_column='VD110', blank=True, null=True)  # Field name made lowercase.
    vd111 = models.IntegerField(db_column='VD111', blank=True, null=True)  # Field name made lowercase.
    vd112 = models.IntegerField(db_column='VD112', blank=True, null=True)  # Field name made lowercase.
    vd113 = models.IntegerField(db_column='VD113', blank=True, null=True)  # Field name made lowercase.
    vd114 = models.IntegerField(db_column='VD114', blank=True, null=True)  # Field name made lowercase.
    vd115 = models.IntegerField(db_column='VD115', blank=True, null=True)  # Field name made lowercase.
    vd116 = models.IntegerField(db_column='VD116', blank=True, null=True)  # Field name made lowercase.
    vd117 = models.IntegerField(db_column='VD117', blank=True, null=True)  # Field name made lowercase.
    vd120 = models.IntegerField(db_column='VD120', blank=True, null=True)  # Field name made lowercase.
    vd121 = models.IntegerField(db_column='VD121', blank=True, null=True)  # Field name made lowercase.
    vd122 = models.IntegerField(db_column='VD122', blank=True, null=True)  # Field name made lowercase.
    vd123 = models.IntegerField(db_column='VD123', blank=True, null=True)  # Field name made lowercase.
    vd124 = models.IntegerField(db_column='VD124', blank=True, null=True)  # Field name made lowercase.
    vd125 = models.IntegerField(db_column='VD125', blank=True, null=True)  # Field name made lowercase.
    vd126 = models.IntegerField(db_column='VD126', blank=True, null=True)  # Field name made lowercase.
    vd127 = models.IntegerField(db_column='VD127', blank=True, null=True)  # Field name made lowercase.
    vd130 = models.IntegerField(db_column='VD130', blank=True, null=True)  # Field name made lowercase.
    vd131 = models.IntegerField(db_column='VD131', blank=True, null=True)  # Field name made lowercase.
    vd132 = models.IntegerField(db_column='VD132', blank=True, null=True)  # Field name made lowercase.
    vd133 = models.IntegerField(db_column='VD133', blank=True, null=True)  # Field name made lowercase.
    vd134 = models.IntegerField(db_column='VD134', blank=True, null=True)  # Field name made lowercase.
    vd135 = models.IntegerField(db_column='VD135', blank=True, null=True)  # Field name made lowercase.
    vd136 = models.IntegerField(db_column='VD136', blank=True, null=True)  # Field name made lowercase.
    vd137 = models.IntegerField(db_column='VD137', blank=True, null=True)  # Field name made lowercase.
    vd140 = models.IntegerField(db_column='VD140', blank=True, null=True)  # Field name made lowercase.
    vd141 = models.IntegerField(db_column='VD141', blank=True, null=True)  # Field name made lowercase.
    vd142 = models.IntegerField(db_column='VD142', blank=True, null=True)  # Field name made lowercase.
    vd143 = models.IntegerField(db_column='VD143', blank=True, null=True)  # Field name made lowercase.
    vd144 = models.IntegerField(db_column='VD144', blank=True, null=True)  # Field name made lowercase.
    vd145 = models.IntegerField(db_column='VD145', blank=True, null=True)  # Field name made lowercase.
    vd146 = models.IntegerField(db_column='VD146', blank=True, null=True)  # Field name made lowercase.
    vd147 = models.IntegerField(db_column='VD147', blank=True, null=True)  # Field name made lowercase.
    vd150 = models.IntegerField(db_column='VD150', blank=True, null=True)  # Field name made lowercase.
    vd151 = models.IntegerField(db_column='VD151', blank=True, null=True)  # Field name made lowercase.
    vd152 = models.IntegerField(db_column='VD152', blank=True, null=True)  # Field name made lowercase.
    vd153 = models.IntegerField(db_column='VD153', blank=True, null=True)  # Field name made lowercase.
    vd154 = models.IntegerField(db_column='VD154', blank=True, null=True)  # Field name made lowercase.
    vd155 = models.IntegerField(db_column='VD155', blank=True, null=True)  # Field name made lowercase.
    vd156 = models.IntegerField(db_column='VD156', blank=True, null=True)  # Field name made lowercase.
    vd157 = models.IntegerField(db_column='VD157', blank=True, null=True)  # Field name made lowercase.
    vd160 = models.IntegerField(db_column='VD160', blank=True, null=True)  # Field name made lowercase.
    vd161 = models.IntegerField(db_column='VD161', blank=True, null=True)  # Field name made lowercase.
    vd162 = models.IntegerField(db_column='VD162', blank=True, null=True)  # Field name made lowercase.
    vd163 = models.IntegerField(db_column='VD163', blank=True, null=True)  # Field name made lowercase.
    vd164 = models.IntegerField(db_column='VD164', blank=True, null=True)  # Field name made lowercase.
    vd165 = models.IntegerField(db_column='VD165', blank=True, null=True)  # Field name made lowercase.
    vd166 = models.IntegerField(db_column='VD166', blank=True, null=True)  # Field name made lowercase.
    vd167 = models.IntegerField(db_column='VD167', blank=True, null=True)  # Field name made lowercase.
    vd170 = models.IntegerField(db_column='VD170', blank=True, null=True)  # Field name made lowercase.
    vd171 = models.IntegerField(db_column='VD171', blank=True, null=True)  # Field name made lowercase.
    vd172 = models.IntegerField(db_column='VD172', blank=True, null=True)  # Field name made lowercase.
    vd173 = models.IntegerField(db_column='VD173', blank=True, null=True)  # Field name made lowercase.
    vd174 = models.IntegerField(db_column='VD174', blank=True, null=True)  # Field name made lowercase.
    vd175 = models.IntegerField(db_column='VD175', blank=True, null=True)  # Field name made lowercase.
    vd176 = models.IntegerField(db_column='VD176', blank=True, null=True)  # Field name made lowercase.
    vd177 = models.IntegerField(db_column='VD177', blank=True, null=True)  # Field name made lowercase.
    vd200 = models.IntegerField(db_column='VD200', blank=True, null=True)  # Field name made lowercase.
    vd201 = models.IntegerField(db_column='VD201', blank=True, null=True)  # Field name made lowercase.
    vd202 = models.IntegerField(db_column='VD202', blank=True, null=True)  # Field name made lowercase.
    vd203 = models.IntegerField(db_column='VD203', blank=True, null=True)  # Field name made lowercase.
    vd204 = models.IntegerField(db_column='VD204', blank=True, null=True)  # Field name made lowercase.
    vd205 = models.IntegerField(db_column='VD205', blank=True, null=True)  # Field name made lowercase.
    vd206 = models.IntegerField(db_column='VD206', blank=True, null=True)  # Field name made lowercase.
    vd207 = models.IntegerField(db_column='VD207', blank=True, null=True)  # Field name made lowercase.
    vd210 = models.IntegerField(db_column='VD210', blank=True, null=True)  # Field name made lowercase.
    vd211 = models.IntegerField(db_column='VD211', blank=True, null=True)  # Field name made lowercase.
    vd212 = models.IntegerField(db_column='VD212', blank=True, null=True)  # Field name made lowercase.
    vd213 = models.IntegerField(db_column='VD213', blank=True, null=True)  # Field name made lowercase.
    vd214 = models.IntegerField(db_column='VD214', blank=True, null=True)  # Field name made lowercase.
    vd215 = models.IntegerField(db_column='VD215', blank=True, null=True)  # Field name made lowercase.
    vd216 = models.IntegerField(db_column='VD216', blank=True, null=True)  # Field name made lowercase.
    vd217 = models.IntegerField(db_column='VD217', blank=True, null=True)  # Field name made lowercase.
    vd220 = models.IntegerField(db_column='VD220', blank=True, null=True)  # Field name made lowercase.
    vd221 = models.IntegerField(db_column='VD221', blank=True, null=True)  # Field name made lowercase.
    vd222 = models.IntegerField(db_column='VD222', blank=True, null=True)  # Field name made lowercase.
    vd223 = models.IntegerField(db_column='VD223', blank=True, null=True)  # Field name made lowercase.
    vd224 = models.IntegerField(db_column='VD224', blank=True, null=True)  # Field name made lowercase.
    vd225 = models.IntegerField(db_column='VD225', blank=True, null=True)  # Field name made lowercase.
    vd226 = models.IntegerField(db_column='VD226', blank=True, null=True)  # Field name made lowercase.
    vd227 = models.IntegerField(db_column='VD227', blank=True, null=True)  # Field name made lowercase.
    vd230 = models.IntegerField(db_column='VD230', blank=True, null=True)  # Field name made lowercase.
    vd231 = models.IntegerField(db_column='VD231', blank=True, null=True)  # Field name made lowercase.
    vd232 = models.IntegerField(db_column='VD232', blank=True, null=True)  # Field name made lowercase.
    vd233 = models.IntegerField(db_column='VD233', blank=True, null=True)  # Field name made lowercase.
    vd234 = models.IntegerField(db_column='VD234', blank=True, null=True)  # Field name made lowercase.
    vd235 = models.IntegerField(db_column='VD235', blank=True, null=True)  # Field name made lowercase.
    vd236 = models.IntegerField(db_column='VD236', blank=True, null=True)  # Field name made lowercase.
    vd237 = models.IntegerField(db_column='VD237', blank=True, null=True)  # Field name made lowercase.
    vd240 = models.IntegerField(db_column='VD240', blank=True, null=True)  # Field name made lowercase.
    vd241 = models.IntegerField(db_column='VD241', blank=True, null=True)  # Field name made lowercase.
    vd242 = models.IntegerField(db_column='VD242', blank=True, null=True)  # Field name made lowercase.
    vd243 = models.IntegerField(db_column='VD243', blank=True, null=True)  # Field name made lowercase.
    vd244 = models.IntegerField(db_column='VD244', blank=True, null=True)  # Field name made lowercase.
    vd245 = models.IntegerField(db_column='VD245', blank=True, null=True)  # Field name made lowercase.
    vd246 = models.IntegerField(db_column='VD246', blank=True, null=True)  # Field name made lowercase.
    vd247 = models.IntegerField(db_column='VD247', blank=True, null=True)  # Field name made lowercase.
    vd250 = models.IntegerField(db_column='VD250', blank=True, null=True)  # Field name made lowercase.
    vd251 = models.IntegerField(db_column='VD251', blank=True, null=True)  # Field name made lowercase.
    vd252 = models.IntegerField(db_column='VD252', blank=True, null=True)  # Field name made lowercase.
    vd253 = models.IntegerField(db_column='VD253', blank=True, null=True)  # Field name made lowercase.
    vd254 = models.IntegerField(db_column='VD254', blank=True, null=True)  # Field name made lowercase.
    vd255 = models.IntegerField(db_column='VD255', blank=True, null=True)  # Field name made lowercase.
    vd256 = models.IntegerField(db_column='VD256', blank=True, null=True)  # Field name made lowercase.
    vd257 = models.IntegerField(db_column='VD257', blank=True, null=True)  # Field name made lowercase.
    vd260 = models.IntegerField(db_column='VD260', blank=True, null=True)  # Field name made lowercase.
    vd261 = models.IntegerField(db_column='VD261', blank=True, null=True)  # Field name made lowercase.
    vd262 = models.IntegerField(db_column='VD262', blank=True, null=True)  # Field name made lowercase.
    vd263 = models.IntegerField(db_column='VD263', blank=True, null=True)  # Field name made lowercase.
    vd264 = models.IntegerField(db_column='VD264', blank=True, null=True)  # Field name made lowercase.
    vd265 = models.IntegerField(db_column='VD265', blank=True, null=True)  # Field name made lowercase.
    vd266 = models.IntegerField(db_column='VD266', blank=True, null=True)  # Field name made lowercase.
    vd267 = models.IntegerField(db_column='VD267', blank=True, null=True)  # Field name made lowercase.
    vd270 = models.IntegerField(db_column='VD270', blank=True, null=True)  # Field name made lowercase.
    vd271 = models.IntegerField(db_column='VD271', blank=True, null=True)  # Field name made lowercase.
    vd272 = models.IntegerField(db_column='VD272', blank=True, null=True)  # Field name made lowercase.
    vd273 = models.IntegerField(db_column='VD273', blank=True, null=True)  # Field name made lowercase.
    vd274 = models.IntegerField(db_column='VD274', blank=True, null=True)  # Field name made lowercase.
    vd275 = models.IntegerField(db_column='VD275', blank=True, null=True)  # Field name made lowercase.
    vd276 = models.IntegerField(db_column='VD276', blank=True, null=True)  # Field name made lowercase.
    vd277 = models.IntegerField(db_column='VD277', blank=True, null=True)  # Field name made lowercase.
    vd300 = models.IntegerField(db_column='VD300', blank=True, null=True)  # Field name made lowercase.
    vd301 = models.IntegerField(db_column='VD301', blank=True, null=True)  # Field name made lowercase.
    vd302 = models.IntegerField(db_column='VD302', blank=True, null=True)  # Field name made lowercase.
    vd303 = models.IntegerField(db_column='VD303', blank=True, null=True)  # Field name made lowercase.
    vd304 = models.IntegerField(db_column='VD304', blank=True, null=True)  # Field name made lowercase.
    vd305 = models.IntegerField(db_column='VD305', blank=True, null=True)  # Field name made lowercase.
    vd306 = models.IntegerField(db_column='VD306', blank=True, null=True)  # Field name made lowercase.
    vd307 = models.IntegerField(db_column='VD307', blank=True, null=True)  # Field name made lowercase.
    vd310 = models.IntegerField(db_column='VD310', blank=True, null=True)  # Field name made lowercase.
    vd311 = models.IntegerField(db_column='VD311', blank=True, null=True)  # Field name made lowercase.
    vd312 = models.IntegerField(db_column='VD312', blank=True, null=True)  # Field name made lowercase.
    vd313 = models.IntegerField(db_column='VD313', blank=True, null=True)  # Field name made lowercase.
    vd314 = models.IntegerField(db_column='VD314', blank=True, null=True)  # Field name made lowercase.
    vd315 = models.IntegerField(db_column='VD315', blank=True, null=True)  # Field name made lowercase.
    vd316 = models.IntegerField(db_column='VD316', blank=True, null=True)  # Field name made lowercase.
    vd317 = models.IntegerField(db_column='VD317', blank=True, null=True)  # Field name made lowercase.
    vd320 = models.IntegerField(db_column='VD320', blank=True, null=True)  # Field name made lowercase.
    vd321 = models.IntegerField(db_column='VD321', blank=True, null=True)  # Field name made lowercase.
    vd322 = models.IntegerField(db_column='VD322', blank=True, null=True)  # Field name made lowercase.
    vd323 = models.IntegerField(db_column='VD323', blank=True, null=True)  # Field name made lowercase.
    vd324 = models.IntegerField(db_column='VD324', blank=True, null=True)  # Field name made lowercase.
    vd325 = models.IntegerField(db_column='VD325', blank=True, null=True)  # Field name made lowercase.
    vd326 = models.IntegerField(db_column='VD326', blank=True, null=True)  # Field name made lowercase.
    vd327 = models.IntegerField(db_column='VD327', blank=True, null=True)  # Field name made lowercase.
    vd330 = models.IntegerField(db_column='VD330', blank=True, null=True)  # Field name made lowercase.
    vd331 = models.IntegerField(db_column='VD331', blank=True, null=True)  # Field name made lowercase.
    vd332 = models.IntegerField(db_column='VD332', blank=True, null=True)  # Field name made lowercase.
    vd333 = models.IntegerField(db_column='VD333', blank=True, null=True)  # Field name made lowercase.
    vd334 = models.IntegerField(db_column='VD334', blank=True, null=True)  # Field name made lowercase.
    vd335 = models.IntegerField(db_column='VD335', blank=True, null=True)  # Field name made lowercase.
    vd336 = models.IntegerField(db_column='VD336', blank=True, null=True)  # Field name made lowercase.
    vd337 = models.IntegerField(db_column='VD337', blank=True, null=True)  # Field name made lowercase.
    vd340 = models.IntegerField(db_column='VD340', blank=True, null=True)  # Field name made lowercase.
    vd341 = models.IntegerField(db_column='VD341', blank=True, null=True)  # Field name made lowercase.
    vd342 = models.IntegerField(db_column='VD342', blank=True, null=True)  # Field name made lowercase.
    vd343 = models.IntegerField(db_column='VD343', blank=True, null=True)  # Field name made lowercase.
    vd344 = models.IntegerField(db_column='VD344', blank=True, null=True)  # Field name made lowercase.
    vd345 = models.IntegerField(db_column='VD345', blank=True, null=True)  # Field name made lowercase.
    vd346 = models.IntegerField(db_column='VD346', blank=True, null=True)  # Field name made lowercase.
    vd347 = models.IntegerField(db_column='VD347', blank=True, null=True)  # Field name made lowercase.
    vd350 = models.IntegerField(db_column='VD350', blank=True, null=True)  # Field name made lowercase.
    vd351 = models.IntegerField(db_column='VD351', blank=True, null=True)  # Field name made lowercase.
    vd352 = models.IntegerField(db_column='VD352', blank=True, null=True)  # Field name made lowercase.
    vd353 = models.IntegerField(db_column='VD353', blank=True, null=True)  # Field name made lowercase.
    vd354 = models.IntegerField(db_column='VD354', blank=True, null=True)  # Field name made lowercase.
    vd355 = models.IntegerField(db_column='VD355', blank=True, null=True)  # Field name made lowercase.
    vd356 = models.IntegerField(db_column='VD356', blank=True, null=True)  # Field name made lowercase.
    vd357 = models.IntegerField(db_column='VD357', blank=True, null=True)  # Field name made lowercase.
    vd360 = models.IntegerField(db_column='VD360', blank=True, null=True)  # Field name made lowercase.
    vd361 = models.IntegerField(db_column='VD361', blank=True, null=True)  # Field name made lowercase.
    vd362 = models.IntegerField(db_column='VD362', blank=True, null=True)  # Field name made lowercase.
    vd363 = models.IntegerField(db_column='VD363', blank=True, null=True)  # Field name made lowercase.
    vd364 = models.IntegerField(db_column='VD364', blank=True, null=True)  # Field name made lowercase.
    vd365 = models.IntegerField(db_column='VD365', blank=True, null=True)  # Field name made lowercase.
    vd366 = models.IntegerField(db_column='VD366', blank=True, null=True)  # Field name made lowercase.
    vd367 = models.IntegerField(db_column='VD367', blank=True, null=True)  # Field name made lowercase.
    vd370 = models.IntegerField(db_column='VD370', blank=True, null=True)  # Field name made lowercase.
    vd371 = models.IntegerField(db_column='VD371', blank=True, null=True)  # Field name made lowercase.
    vd372 = models.IntegerField(db_column='VD372', blank=True, null=True)  # Field name made lowercase.
    vd373 = models.IntegerField(db_column='VD373', blank=True, null=True)  # Field name made lowercase.
    vd374 = models.IntegerField(db_column='VD374', blank=True, null=True)  # Field name made lowercase.
    vd375 = models.IntegerField(db_column='VD375', blank=True, null=True)  # Field name made lowercase.
    vd376 = models.IntegerField(db_column='VD376', blank=True, null=True)  # Field name made lowercase.
    vd377 = models.IntegerField(db_column='VD377', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'L110KVD_B1'


class L110KvdB2(models.Model):
    id_item = models.AutoField(db_column='ID_ITEM', primary_key=True)  # Field name made lowercase.
    timepoint = models.DateTimeField(db_column='TIMEPOINT', unique=True, blank=True,
                                     null=True)  # Field name made lowercase.
    vd000 = models.IntegerField(db_column='VD000', blank=True, null=True)  # Field name made lowercase.
    vd001 = models.IntegerField(db_column='VD001', blank=True, null=True)  # Field name made lowercase.
    vd002 = models.IntegerField(db_column='VD002', blank=True, null=True)  # Field name made lowercase.
    vd003 = models.IntegerField(db_column='VD003', blank=True, null=True)  # Field name made lowercase.
    vd004 = models.IntegerField(db_column='VD004', blank=True, null=True)  # Field name made lowercase.
    vd005 = models.IntegerField(db_column='VD005', blank=True, null=True)  # Field name made lowercase.
    vd006 = models.IntegerField(db_column='VD006', blank=True, null=True)  # Field name made lowercase.
    vd007 = models.IntegerField(db_column='VD007', blank=True, null=True)  # Field name made lowercase.
    vd010 = models.IntegerField(db_column='VD010', blank=True, null=True)  # Field name made lowercase.
    vd011 = models.IntegerField(db_column='VD011', blank=True, null=True)  # Field name made lowercase.
    vd012 = models.IntegerField(db_column='VD012', blank=True, null=True)  # Field name made lowercase.
    vd013 = models.IntegerField(db_column='VD013', blank=True, null=True)  # Field name made lowercase.
    vd014 = models.IntegerField(db_column='VD014', blank=True, null=True)  # Field name made lowercase.
    vd015 = models.IntegerField(db_column='VD015', blank=True, null=True)  # Field name made lowercase.
    vd016 = models.IntegerField(db_column='VD016', blank=True, null=True)  # Field name made lowercase.
    vd017 = models.IntegerField(db_column='VD017', blank=True, null=True)  # Field name made lowercase.
    vd020 = models.IntegerField(db_column='VD020', blank=True, null=True)  # Field name made lowercase.
    vd021 = models.IntegerField(db_column='VD021', blank=True, null=True)  # Field name made lowercase.
    vd022 = models.IntegerField(db_column='VD022', blank=True, null=True)  # Field name made lowercase.
    vd023 = models.IntegerField(db_column='VD023', blank=True, null=True)  # Field name made lowercase.
    vd024 = models.IntegerField(db_column='VD024', blank=True, null=True)  # Field name made lowercase.
    vd025 = models.IntegerField(db_column='VD025', blank=True, null=True)  # Field name made lowercase.
    vd026 = models.IntegerField(db_column='VD026', blank=True, null=True)  # Field name made lowercase.
    vd027 = models.IntegerField(db_column='VD027', blank=True, null=True)  # Field name made lowercase.
    vd030 = models.IntegerField(db_column='VD030', blank=True, null=True)  # Field name made lowercase.
    vd031 = models.IntegerField(db_column='VD031', blank=True, null=True)  # Field name made lowercase.
    vd032 = models.IntegerField(db_column='VD032', blank=True, null=True)  # Field name made lowercase.
    vd033 = models.IntegerField(db_column='VD033', blank=True, null=True)  # Field name made lowercase.
    vd034 = models.IntegerField(db_column='VD034', blank=True, null=True)  # Field name made lowercase.
    vd035 = models.IntegerField(db_column='VD035', blank=True, null=True)  # Field name made lowercase.
    vd036 = models.IntegerField(db_column='VD036', blank=True, null=True)  # Field name made lowercase.
    vd037 = models.IntegerField(db_column='VD037', blank=True, null=True)  # Field name made lowercase.
    vd040 = models.IntegerField(db_column='VD040', blank=True, null=True)  # Field name made lowercase.
    vd041 = models.IntegerField(db_column='VD041', blank=True, null=True)  # Field name made lowercase.
    vd042 = models.IntegerField(db_column='VD042', blank=True, null=True)  # Field name made lowercase.
    vd043 = models.IntegerField(db_column='VD043', blank=True, null=True)  # Field name made lowercase.
    vd044 = models.IntegerField(db_column='VD044', blank=True, null=True)  # Field name made lowercase.
    vd045 = models.IntegerField(db_column='VD045', blank=True, null=True)  # Field name made lowercase.
    vd046 = models.IntegerField(db_column='VD046', blank=True, null=True)  # Field name made lowercase.
    vd047 = models.IntegerField(db_column='VD047', blank=True, null=True)  # Field name made lowercase.
    vd050 = models.IntegerField(db_column='VD050', blank=True, null=True)  # Field name made lowercase.
    vd051 = models.IntegerField(db_column='VD051', blank=True, null=True)  # Field name made lowercase.
    vd052 = models.IntegerField(db_column='VD052', blank=True, null=True)  # Field name made lowercase.
    vd053 = models.IntegerField(db_column='VD053', blank=True, null=True)  # Field name made lowercase.
    vd054 = models.IntegerField(db_column='VD054', blank=True, null=True)  # Field name made lowercase.
    vd055 = models.IntegerField(db_column='VD055', blank=True, null=True)  # Field name made lowercase.
    vd056 = models.IntegerField(db_column='VD056', blank=True, null=True)  # Field name made lowercase.
    vd057 = models.IntegerField(db_column='VD057', blank=True, null=True)  # Field name made lowercase.
    vd060 = models.IntegerField(db_column='VD060', blank=True, null=True)  # Field name made lowercase.
    vd061 = models.IntegerField(db_column='VD061', blank=True, null=True)  # Field name made lowercase.
    vd062 = models.IntegerField(db_column='VD062', blank=True, null=True)  # Field name made lowercase.
    vd063 = models.IntegerField(db_column='VD063', blank=True, null=True)  # Field name made lowercase.
    vd064 = models.IntegerField(db_column='VD064', blank=True, null=True)  # Field name made lowercase.
    vd065 = models.IntegerField(db_column='VD065', blank=True, null=True)  # Field name made lowercase.
    vd066 = models.IntegerField(db_column='VD066', blank=True, null=True)  # Field name made lowercase.
    vd067 = models.IntegerField(db_column='VD067', blank=True, null=True)  # Field name made lowercase.
    vd070 = models.IntegerField(db_column='VD070', blank=True, null=True)  # Field name made lowercase.
    vd071 = models.IntegerField(db_column='VD071', blank=True, null=True)  # Field name made lowercase.
    vd072 = models.IntegerField(db_column='VD072', blank=True, null=True)  # Field name made lowercase.
    vd073 = models.IntegerField(db_column='VD073', blank=True, null=True)  # Field name made lowercase.
    vd074 = models.IntegerField(db_column='VD074', blank=True, null=True)  # Field name made lowercase.
    vd075 = models.IntegerField(db_column='VD075', blank=True, null=True)  # Field name made lowercase.
    vd076 = models.IntegerField(db_column='VD076', blank=True, null=True)  # Field name made lowercase.
    vd077 = models.IntegerField(db_column='VD077', blank=True, null=True)  # Field name made lowercase.
    vd100 = models.IntegerField(db_column='VD100', blank=True, null=True)  # Field name made lowercase.
    vd101 = models.IntegerField(db_column='VD101', blank=True, null=True)  # Field name made lowercase.
    vd102 = models.IntegerField(db_column='VD102', blank=True, null=True)  # Field name made lowercase.
    vd103 = models.IntegerField(db_column='VD103', blank=True, null=True)  # Field name made lowercase.
    vd104 = models.IntegerField(db_column='VD104', blank=True, null=True)  # Field name made lowercase.
    vd105 = models.IntegerField(db_column='VD105', blank=True, null=True)  # Field name made lowercase.
    vd106 = models.IntegerField(db_column='VD106', blank=True, null=True)  # Field name made lowercase.
    vd107 = models.IntegerField(db_column='VD107', blank=True, null=True)  # Field name made lowercase.
    vd110 = models.IntegerField(db_column='VD110', blank=True, null=True)  # Field name made lowercase.
    vd111 = models.IntegerField(db_column='VD111', blank=True, null=True)  # Field name made lowercase.
    vd112 = models.IntegerField(db_column='VD112', blank=True, null=True)  # Field name made lowercase.
    vd113 = models.IntegerField(db_column='VD113', blank=True, null=True)  # Field name made lowercase.
    vd114 = models.IntegerField(db_column='VD114', blank=True, null=True)  # Field name made lowercase.
    vd115 = models.IntegerField(db_column='VD115', blank=True, null=True)  # Field name made lowercase.
    vd116 = models.IntegerField(db_column='VD116', blank=True, null=True)  # Field name made lowercase.
    vd117 = models.IntegerField(db_column='VD117', blank=True, null=True)  # Field name made lowercase.
    vd120 = models.IntegerField(db_column='VD120', blank=True, null=True)  # Field name made lowercase.
    vd121 = models.IntegerField(db_column='VD121', blank=True, null=True)  # Field name made lowercase.
    vd122 = models.IntegerField(db_column='VD122', blank=True, null=True)  # Field name made lowercase.
    vd123 = models.IntegerField(db_column='VD123', blank=True, null=True)  # Field name made lowercase.
    vd124 = models.IntegerField(db_column='VD124', blank=True, null=True)  # Field name made lowercase.
    vd125 = models.IntegerField(db_column='VD125', blank=True, null=True)  # Field name made lowercase.
    vd126 = models.IntegerField(db_column='VD126', blank=True, null=True)  # Field name made lowercase.
    vd127 = models.IntegerField(db_column='VD127', blank=True, null=True)  # Field name made lowercase.
    vd130 = models.IntegerField(db_column='VD130', blank=True, null=True)  # Field name made lowercase.
    vd131 = models.IntegerField(db_column='VD131', blank=True, null=True)  # Field name made lowercase.
    vd132 = models.IntegerField(db_column='VD132', blank=True, null=True)  # Field name made lowercase.
    vd133 = models.IntegerField(db_column='VD133', blank=True, null=True)  # Field name made lowercase.
    vd134 = models.IntegerField(db_column='VD134', blank=True, null=True)  # Field name made lowercase.
    vd135 = models.IntegerField(db_column='VD135', blank=True, null=True)  # Field name made lowercase.
    vd136 = models.IntegerField(db_column='VD136', blank=True, null=True)  # Field name made lowercase.
    vd137 = models.IntegerField(db_column='VD137', blank=True, null=True)  # Field name made lowercase.
    vd140 = models.IntegerField(db_column='VD140', blank=True, null=True)  # Field name made lowercase.
    vd141 = models.IntegerField(db_column='VD141', blank=True, null=True)  # Field name made lowercase.
    vd142 = models.IntegerField(db_column='VD142', blank=True, null=True)  # Field name made lowercase.
    vd143 = models.IntegerField(db_column='VD143', blank=True, null=True)  # Field name made lowercase.
    vd144 = models.IntegerField(db_column='VD144', blank=True, null=True)  # Field name made lowercase.
    vd145 = models.IntegerField(db_column='VD145', blank=True, null=True)  # Field name made lowercase.
    vd146 = models.IntegerField(db_column='VD146', blank=True, null=True)  # Field name made lowercase.
    vd147 = models.IntegerField(db_column='VD147', blank=True, null=True)  # Field name made lowercase.
    vd150 = models.IntegerField(db_column='VD150', blank=True, null=True)  # Field name made lowercase.
    vd151 = models.IntegerField(db_column='VD151', blank=True, null=True)  # Field name made lowercase.
    vd152 = models.IntegerField(db_column='VD152', blank=True, null=True)  # Field name made lowercase.
    vd153 = models.IntegerField(db_column='VD153', blank=True, null=True)  # Field name made lowercase.
    vd154 = models.IntegerField(db_column='VD154', blank=True, null=True)  # Field name made lowercase.
    vd155 = models.IntegerField(db_column='VD155', blank=True, null=True)  # Field name made lowercase.
    vd156 = models.IntegerField(db_column='VD156', blank=True, null=True)  # Field name made lowercase.
    vd157 = models.IntegerField(db_column='VD157', blank=True, null=True)  # Field name made lowercase.
    vd160 = models.IntegerField(db_column='VD160', blank=True, null=True)  # Field name made lowercase.
    vd161 = models.IntegerField(db_column='VD161', blank=True, null=True)  # Field name made lowercase.
    vd162 = models.IntegerField(db_column='VD162', blank=True, null=True)  # Field name made lowercase.
    vd163 = models.IntegerField(db_column='VD163', blank=True, null=True)  # Field name made lowercase.
    vd164 = models.IntegerField(db_column='VD164', blank=True, null=True)  # Field name made lowercase.
    vd165 = models.IntegerField(db_column='VD165', blank=True, null=True)  # Field name made lowercase.
    vd166 = models.IntegerField(db_column='VD166', blank=True, null=True)  # Field name made lowercase.
    vd167 = models.IntegerField(db_column='VD167', blank=True, null=True)  # Field name made lowercase.
    vd170 = models.IntegerField(db_column='VD170', blank=True, null=True)  # Field name made lowercase.
    vd171 = models.IntegerField(db_column='VD171', blank=True, null=True)  # Field name made lowercase.
    vd172 = models.IntegerField(db_column='VD172', blank=True, null=True)  # Field name made lowercase.
    vd173 = models.IntegerField(db_column='VD173', blank=True, null=True)  # Field name made lowercase.
    vd174 = models.IntegerField(db_column='VD174', blank=True, null=True)  # Field name made lowercase.
    vd175 = models.IntegerField(db_column='VD175', blank=True, null=True)  # Field name made lowercase.
    vd176 = models.IntegerField(db_column='VD176', blank=True, null=True)  # Field name made lowercase.
    vd177 = models.IntegerField(db_column='VD177', blank=True, null=True)  # Field name made lowercase.
    vd200 = models.IntegerField(db_column='VD200', blank=True, null=True)  # Field name made lowercase.
    vd201 = models.IntegerField(db_column='VD201', blank=True, null=True)  # Field name made lowercase.
    vd202 = models.IntegerField(db_column='VD202', blank=True, null=True)  # Field name made lowercase.
    vd203 = models.IntegerField(db_column='VD203', blank=True, null=True)  # Field name made lowercase.
    vd204 = models.IntegerField(db_column='VD204', blank=True, null=True)  # Field name made lowercase.
    vd205 = models.IntegerField(db_column='VD205', blank=True, null=True)  # Field name made lowercase.
    vd206 = models.IntegerField(db_column='VD206', blank=True, null=True)  # Field name made lowercase.
    vd207 = models.IntegerField(db_column='VD207', blank=True, null=True)  # Field name made lowercase.
    vd210 = models.IntegerField(db_column='VD210', blank=True, null=True)  # Field name made lowercase.
    vd211 = models.IntegerField(db_column='VD211', blank=True, null=True)  # Field name made lowercase.
    vd212 = models.IntegerField(db_column='VD212', blank=True, null=True)  # Field name made lowercase.
    vd213 = models.IntegerField(db_column='VD213', blank=True, null=True)  # Field name made lowercase.
    vd214 = models.IntegerField(db_column='VD214', blank=True, null=True)  # Field name made lowercase.
    vd215 = models.IntegerField(db_column='VD215', blank=True, null=True)  # Field name made lowercase.
    vd216 = models.IntegerField(db_column='VD216', blank=True, null=True)  # Field name made lowercase.
    vd217 = models.IntegerField(db_column='VD217', blank=True, null=True)  # Field name made lowercase.
    vd220 = models.IntegerField(db_column='VD220', blank=True, null=True)  # Field name made lowercase.
    vd221 = models.IntegerField(db_column='VD221', blank=True, null=True)  # Field name made lowercase.
    vd222 = models.IntegerField(db_column='VD222', blank=True, null=True)  # Field name made lowercase.
    vd223 = models.IntegerField(db_column='VD223', blank=True, null=True)  # Field name made lowercase.
    vd224 = models.IntegerField(db_column='VD224', blank=True, null=True)  # Field name made lowercase.
    vd225 = models.IntegerField(db_column='VD225', blank=True, null=True)  # Field name made lowercase.
    vd226 = models.IntegerField(db_column='VD226', blank=True, null=True)  # Field name made lowercase.
    vd227 = models.IntegerField(db_column='VD227', blank=True, null=True)  # Field name made lowercase.
    vd230 = models.IntegerField(db_column='VD230', blank=True, null=True)  # Field name made lowercase.
    vd231 = models.IntegerField(db_column='VD231', blank=True, null=True)  # Field name made lowercase.
    vd232 = models.IntegerField(db_column='VD232', blank=True, null=True)  # Field name made lowercase.
    vd233 = models.IntegerField(db_column='VD233', blank=True, null=True)  # Field name made lowercase.
    vd234 = models.IntegerField(db_column='VD234', blank=True, null=True)  # Field name made lowercase.
    vd235 = models.IntegerField(db_column='VD235', blank=True, null=True)  # Field name made lowercase.
    vd236 = models.IntegerField(db_column='VD236', blank=True, null=True)  # Field name made lowercase.
    vd237 = models.IntegerField(db_column='VD237', blank=True, null=True)  # Field name made lowercase.
    vd240 = models.IntegerField(db_column='VD240', blank=True, null=True)  # Field name made lowercase.
    vd241 = models.IntegerField(db_column='VD241', blank=True, null=True)  # Field name made lowercase.
    vd242 = models.IntegerField(db_column='VD242', blank=True, null=True)  # Field name made lowercase.
    vd243 = models.IntegerField(db_column='VD243', blank=True, null=True)  # Field name made lowercase.
    vd244 = models.IntegerField(db_column='VD244', blank=True, null=True)  # Field name made lowercase.
    vd245 = models.IntegerField(db_column='VD245', blank=True, null=True)  # Field name made lowercase.
    vd246 = models.IntegerField(db_column='VD246', blank=True, null=True)  # Field name made lowercase.
    vd247 = models.IntegerField(db_column='VD247', blank=True, null=True)  # Field name made lowercase.
    vd250 = models.IntegerField(db_column='VD250', blank=True, null=True)  # Field name made lowercase.
    vd251 = models.IntegerField(db_column='VD251', blank=True, null=True)  # Field name made lowercase.
    vd252 = models.IntegerField(db_column='VD252', blank=True, null=True)  # Field name made lowercase.
    vd253 = models.IntegerField(db_column='VD253', blank=True, null=True)  # Field name made lowercase.
    vd254 = models.IntegerField(db_column='VD254', blank=True, null=True)  # Field name made lowercase.
    vd255 = models.IntegerField(db_column='VD255', blank=True, null=True)  # Field name made lowercase.
    vd256 = models.IntegerField(db_column='VD256', blank=True, null=True)  # Field name made lowercase.
    vd257 = models.IntegerField(db_column='VD257', blank=True, null=True)  # Field name made lowercase.
    vd260 = models.IntegerField(db_column='VD260', blank=True, null=True)  # Field name made lowercase.
    vd261 = models.IntegerField(db_column='VD261', blank=True, null=True)  # Field name made lowercase.
    vd262 = models.IntegerField(db_column='VD262', blank=True, null=True)  # Field name made lowercase.
    vd263 = models.IntegerField(db_column='VD263', blank=True, null=True)  # Field name made lowercase.
    vd264 = models.IntegerField(db_column='VD264', blank=True, null=True)  # Field name made lowercase.
    vd265 = models.IntegerField(db_column='VD265', blank=True, null=True)  # Field name made lowercase.
    vd266 = models.IntegerField(db_column='VD266', blank=True, null=True)  # Field name made lowercase.
    vd267 = models.IntegerField(db_column='VD267', blank=True, null=True)  # Field name made lowercase.
    vd270 = models.IntegerField(db_column='VD270', blank=True, null=True)  # Field name made lowercase.
    vd271 = models.IntegerField(db_column='VD271', blank=True, null=True)  # Field name made lowercase.
    vd272 = models.IntegerField(db_column='VD272', blank=True, null=True)  # Field name made lowercase.
    vd273 = models.IntegerField(db_column='VD273', blank=True, null=True)  # Field name made lowercase.
    vd274 = models.IntegerField(db_column='VD274', blank=True, null=True)  # Field name made lowercase.
    vd275 = models.IntegerField(db_column='VD275', blank=True, null=True)  # Field name made lowercase.
    vd276 = models.IntegerField(db_column='VD276', blank=True, null=True)  # Field name made lowercase.
    vd277 = models.IntegerField(db_column='VD277', blank=True, null=True)  # Field name made lowercase.
    vd300 = models.IntegerField(db_column='VD300', blank=True, null=True)  # Field name made lowercase.
    vd301 = models.IntegerField(db_column='VD301', blank=True, null=True)  # Field name made lowercase.
    vd302 = models.IntegerField(db_column='VD302', blank=True, null=True)  # Field name made lowercase.
    vd303 = models.IntegerField(db_column='VD303', blank=True, null=True)  # Field name made lowercase.
    vd304 = models.IntegerField(db_column='VD304', blank=True, null=True)  # Field name made lowercase.
    vd305 = models.IntegerField(db_column='VD305', blank=True, null=True)  # Field name made lowercase.
    vd306 = models.IntegerField(db_column='VD306', blank=True, null=True)  # Field name made lowercase.
    vd307 = models.IntegerField(db_column='VD307', blank=True, null=True)  # Field name made lowercase.
    vd310 = models.IntegerField(db_column='VD310', blank=True, null=True)  # Field name made lowercase.
    vd311 = models.IntegerField(db_column='VD311', blank=True, null=True)  # Field name made lowercase.
    vd312 = models.IntegerField(db_column='VD312', blank=True, null=True)  # Field name made lowercase.
    vd313 = models.IntegerField(db_column='VD313', blank=True, null=True)  # Field name made lowercase.
    vd314 = models.IntegerField(db_column='VD314', blank=True, null=True)  # Field name made lowercase.
    vd315 = models.IntegerField(db_column='VD315', blank=True, null=True)  # Field name made lowercase.
    vd316 = models.IntegerField(db_column='VD316', blank=True, null=True)  # Field name made lowercase.
    vd317 = models.IntegerField(db_column='VD317', blank=True, null=True)  # Field name made lowercase.
    vd320 = models.IntegerField(db_column='VD320', blank=True, null=True)  # Field name made lowercase.
    vd321 = models.IntegerField(db_column='VD321', blank=True, null=True)  # Field name made lowercase.
    vd322 = models.IntegerField(db_column='VD322', blank=True, null=True)  # Field name made lowercase.
    vd323 = models.IntegerField(db_column='VD323', blank=True, null=True)  # Field name made lowercase.
    vd324 = models.IntegerField(db_column='VD324', blank=True, null=True)  # Field name made lowercase.
    vd325 = models.IntegerField(db_column='VD325', blank=True, null=True)  # Field name made lowercase.
    vd326 = models.IntegerField(db_column='VD326', blank=True, null=True)  # Field name made lowercase.
    vd327 = models.IntegerField(db_column='VD327', blank=True, null=True)  # Field name made lowercase.
    vd330 = models.IntegerField(db_column='VD330', blank=True, null=True)  # Field name made lowercase.
    vd331 = models.IntegerField(db_column='VD331', blank=True, null=True)  # Field name made lowercase.
    vd332 = models.IntegerField(db_column='VD332', blank=True, null=True)  # Field name made lowercase.
    vd333 = models.IntegerField(db_column='VD333', blank=True, null=True)  # Field name made lowercase.
    vd334 = models.IntegerField(db_column='VD334', blank=True, null=True)  # Field name made lowercase.
    vd335 = models.IntegerField(db_column='VD335', blank=True, null=True)  # Field name made lowercase.
    vd336 = models.IntegerField(db_column='VD336', blank=True, null=True)  # Field name made lowercase.
    vd337 = models.IntegerField(db_column='VD337', blank=True, null=True)  # Field name made lowercase.
    vd340 = models.IntegerField(db_column='VD340', blank=True, null=True)  # Field name made lowercase.
    vd341 = models.IntegerField(db_column='VD341', blank=True, null=True)  # Field name made lowercase.
    vd342 = models.IntegerField(db_column='VD342', blank=True, null=True)  # Field name made lowercase.
    vd343 = models.IntegerField(db_column='VD343', blank=True, null=True)  # Field name made lowercase.
    vd344 = models.IntegerField(db_column='VD344', blank=True, null=True)  # Field name made lowercase.
    vd345 = models.IntegerField(db_column='VD345', blank=True, null=True)  # Field name made lowercase.
    vd346 = models.IntegerField(db_column='VD346', blank=True, null=True)  # Field name made lowercase.
    vd347 = models.IntegerField(db_column='VD347', blank=True, null=True)  # Field name made lowercase.
    vd350 = models.IntegerField(db_column='VD350', blank=True, null=True)  # Field name made lowercase.
    vd351 = models.IntegerField(db_column='VD351', blank=True, null=True)  # Field name made lowercase.
    vd352 = models.IntegerField(db_column='VD352', blank=True, null=True)  # Field name made lowercase.
    vd353 = models.IntegerField(db_column='VD353', blank=True, null=True)  # Field name made lowercase.
    vd354 = models.IntegerField(db_column='VD354', blank=True, null=True)  # Field name made lowercase.
    vd355 = models.IntegerField(db_column='VD355', blank=True, null=True)  # Field name made lowercase.
    vd356 = models.IntegerField(db_column='VD356', blank=True, null=True)  # Field name made lowercase.
    vd357 = models.IntegerField(db_column='VD357', blank=True, null=True)  # Field name made lowercase.
    vd360 = models.IntegerField(db_column='VD360', blank=True, null=True)  # Field name made lowercase.
    vd361 = models.IntegerField(db_column='VD361', blank=True, null=True)  # Field name made lowercase.
    vd362 = models.IntegerField(db_column='VD362', blank=True, null=True)  # Field name made lowercase.
    vd363 = models.IntegerField(db_column='VD363', blank=True, null=True)  # Field name made lowercase.
    vd364 = models.IntegerField(db_column='VD364', blank=True, null=True)  # Field name made lowercase.
    vd365 = models.IntegerField(db_column='VD365', blank=True, null=True)  # Field name made lowercase.
    vd366 = models.IntegerField(db_column='VD366', blank=True, null=True)  # Field name made lowercase.
    vd367 = models.IntegerField(db_column='VD367', blank=True, null=True)  # Field name made lowercase.
    vd370 = models.IntegerField(db_column='VD370', blank=True, null=True)  # Field name made lowercase.
    vd371 = models.IntegerField(db_column='VD371', blank=True, null=True)  # Field name made lowercase.
    vd372 = models.IntegerField(db_column='VD372', blank=True, null=True)  # Field name made lowercase.
    vd373 = models.IntegerField(db_column='VD373', blank=True, null=True)  # Field name made lowercase.
    vd374 = models.IntegerField(db_column='VD374', blank=True, null=True)  # Field name made lowercase.
    vd375 = models.IntegerField(db_column='VD375', blank=True, null=True)  # Field name made lowercase.
    vd376 = models.IntegerField(db_column='VD376', blank=True, null=True)  # Field name made lowercase.
    vd377 = models.IntegerField(db_column='VD377', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'L110KVD_B2'


class L110KvdB3(models.Model):
    id_item = models.AutoField(db_column='ID_ITEM', primary_key=True)  # Field name made lowercase.
    timepoint = models.DateTimeField(db_column='TIMEPOINT', unique=True, blank=True,
                                     null=True)  # Field name made lowercase.
    vd000 = models.IntegerField(db_column='VD000', blank=True, null=True)  # Field name made lowercase.
    vd001 = models.IntegerField(db_column='VD001', blank=True, null=True)  # Field name made lowercase.
    vd002 = models.IntegerField(db_column='VD002', blank=True, null=True)  # Field name made lowercase.
    vd003 = models.IntegerField(db_column='VD003', blank=True, null=True)  # Field name made lowercase.
    vd004 = models.IntegerField(db_column='VD004', blank=True, null=True)  # Field name made lowercase.
    vd005 = models.IntegerField(db_column='VD005', blank=True, null=True)  # Field name made lowercase.
    vd006 = models.IntegerField(db_column='VD006', blank=True, null=True)  # Field name made lowercase.
    vd007 = models.IntegerField(db_column='VD007', blank=True, null=True)  # Field name made lowercase.
    vd010 = models.IntegerField(db_column='VD010', blank=True, null=True)  # Field name made lowercase.
    vd011 = models.IntegerField(db_column='VD011', blank=True, null=True)  # Field name made lowercase.
    vd012 = models.IntegerField(db_column='VD012', blank=True, null=True)  # Field name made lowercase.
    vd013 = models.IntegerField(db_column='VD013', blank=True, null=True)  # Field name made lowercase.
    vd014 = models.IntegerField(db_column='VD014', blank=True, null=True)  # Field name made lowercase.
    vd015 = models.IntegerField(db_column='VD015', blank=True, null=True)  # Field name made lowercase.
    vd016 = models.IntegerField(db_column='VD016', blank=True, null=True)  # Field name made lowercase.
    vd017 = models.IntegerField(db_column='VD017', blank=True, null=True)  # Field name made lowercase.
    vd020 = models.IntegerField(db_column='VD020', blank=True, null=True)  # Field name made lowercase.
    vd021 = models.IntegerField(db_column='VD021', blank=True, null=True)  # Field name made lowercase.
    vd022 = models.IntegerField(db_column='VD022', blank=True, null=True)  # Field name made lowercase.
    vd023 = models.IntegerField(db_column='VD023', blank=True, null=True)  # Field name made lowercase.
    vd024 = models.IntegerField(db_column='VD024', blank=True, null=True)  # Field name made lowercase.
    vd025 = models.IntegerField(db_column='VD025', blank=True, null=True)  # Field name made lowercase.
    vd026 = models.IntegerField(db_column='VD026', blank=True, null=True)  # Field name made lowercase.
    vd027 = models.IntegerField(db_column='VD027', blank=True, null=True)  # Field name made lowercase.
    vd030 = models.IntegerField(db_column='VD030', blank=True, null=True)  # Field name made lowercase.
    vd031 = models.IntegerField(db_column='VD031', blank=True, null=True)  # Field name made lowercase.
    vd032 = models.IntegerField(db_column='VD032', blank=True, null=True)  # Field name made lowercase.
    vd033 = models.IntegerField(db_column='VD033', blank=True, null=True)  # Field name made lowercase.
    vd034 = models.IntegerField(db_column='VD034', blank=True, null=True)  # Field name made lowercase.
    vd035 = models.IntegerField(db_column='VD035', blank=True, null=True)  # Field name made lowercase.
    vd036 = models.IntegerField(db_column='VD036', blank=True, null=True)  # Field name made lowercase.
    vd037 = models.IntegerField(db_column='VD037', blank=True, null=True)  # Field name made lowercase.
    vd040 = models.IntegerField(db_column='VD040', blank=True, null=True)  # Field name made lowercase.
    vd041 = models.IntegerField(db_column='VD041', blank=True, null=True)  # Field name made lowercase.
    vd042 = models.IntegerField(db_column='VD042', blank=True, null=True)  # Field name made lowercase.
    vd043 = models.IntegerField(db_column='VD043', blank=True, null=True)  # Field name made lowercase.
    vd044 = models.IntegerField(db_column='VD044', blank=True, null=True)  # Field name made lowercase.
    vd045 = models.IntegerField(db_column='VD045', blank=True, null=True)  # Field name made lowercase.
    vd046 = models.IntegerField(db_column='VD046', blank=True, null=True)  # Field name made lowercase.
    vd047 = models.IntegerField(db_column='VD047', blank=True, null=True)  # Field name made lowercase.
    vd050 = models.IntegerField(db_column='VD050', blank=True, null=True)  # Field name made lowercase.
    vd051 = models.IntegerField(db_column='VD051', blank=True, null=True)  # Field name made lowercase.
    vd052 = models.IntegerField(db_column='VD052', blank=True, null=True)  # Field name made lowercase.
    vd053 = models.IntegerField(db_column='VD053', blank=True, null=True)  # Field name made lowercase.
    vd054 = models.IntegerField(db_column='VD054', blank=True, null=True)  # Field name made lowercase.
    vd055 = models.IntegerField(db_column='VD055', blank=True, null=True)  # Field name made lowercase.
    vd056 = models.IntegerField(db_column='VD056', blank=True, null=True)  # Field name made lowercase.
    vd057 = models.IntegerField(db_column='VD057', blank=True, null=True)  # Field name made lowercase.
    vd060 = models.IntegerField(db_column='VD060', blank=True, null=True)  # Field name made lowercase.
    vd061 = models.IntegerField(db_column='VD061', blank=True, null=True)  # Field name made lowercase.
    vd062 = models.IntegerField(db_column='VD062', blank=True, null=True)  # Field name made lowercase.
    vd063 = models.IntegerField(db_column='VD063', blank=True, null=True)  # Field name made lowercase.
    vd064 = models.IntegerField(db_column='VD064', blank=True, null=True)  # Field name made lowercase.
    vd065 = models.IntegerField(db_column='VD065', blank=True, null=True)  # Field name made lowercase.
    vd066 = models.IntegerField(db_column='VD066', blank=True, null=True)  # Field name made lowercase.
    vd067 = models.IntegerField(db_column='VD067', blank=True, null=True)  # Field name made lowercase.
    vd070 = models.IntegerField(db_column='VD070', blank=True, null=True)  # Field name made lowercase.
    vd071 = models.IntegerField(db_column='VD071', blank=True, null=True)  # Field name made lowercase.
    vd072 = models.IntegerField(db_column='VD072', blank=True, null=True)  # Field name made lowercase.
    vd073 = models.IntegerField(db_column='VD073', blank=True, null=True)  # Field name made lowercase.
    vd074 = models.IntegerField(db_column='VD074', blank=True, null=True)  # Field name made lowercase.
    vd075 = models.IntegerField(db_column='VD075', blank=True, null=True)  # Field name made lowercase.
    vd076 = models.IntegerField(db_column='VD076', blank=True, null=True)  # Field name made lowercase.
    vd077 = models.IntegerField(db_column='VD077', blank=True, null=True)  # Field name made lowercase.
    vd100 = models.IntegerField(db_column='VD100', blank=True, null=True)  # Field name made lowercase.
    vd101 = models.IntegerField(db_column='VD101', blank=True, null=True)  # Field name made lowercase.
    vd102 = models.IntegerField(db_column='VD102', blank=True, null=True)  # Field name made lowercase.
    vd103 = models.IntegerField(db_column='VD103', blank=True, null=True)  # Field name made lowercase.
    vd104 = models.IntegerField(db_column='VD104', blank=True, null=True)  # Field name made lowercase.
    vd105 = models.IntegerField(db_column='VD105', blank=True, null=True)  # Field name made lowercase.
    vd106 = models.IntegerField(db_column='VD106', blank=True, null=True)  # Field name made lowercase.
    vd107 = models.IntegerField(db_column='VD107', blank=True, null=True)  # Field name made lowercase.
    vd110 = models.IntegerField(db_column='VD110', blank=True, null=True)  # Field name made lowercase.
    vd111 = models.IntegerField(db_column='VD111', blank=True, null=True)  # Field name made lowercase.
    vd112 = models.IntegerField(db_column='VD112', blank=True, null=True)  # Field name made lowercase.
    vd113 = models.IntegerField(db_column='VD113', blank=True, null=True)  # Field name made lowercase.
    vd114 = models.IntegerField(db_column='VD114', blank=True, null=True)  # Field name made lowercase.
    vd115 = models.IntegerField(db_column='VD115', blank=True, null=True)  # Field name made lowercase.
    vd116 = models.IntegerField(db_column='VD116', blank=True, null=True)  # Field name made lowercase.
    vd117 = models.IntegerField(db_column='VD117', blank=True, null=True)  # Field name made lowercase.
    vd120 = models.IntegerField(db_column='VD120', blank=True, null=True)  # Field name made lowercase.
    vd121 = models.IntegerField(db_column='VD121', blank=True, null=True)  # Field name made lowercase.
    vd122 = models.IntegerField(db_column='VD122', blank=True, null=True)  # Field name made lowercase.
    vd123 = models.IntegerField(db_column='VD123', blank=True, null=True)  # Field name made lowercase.
    vd124 = models.IntegerField(db_column='VD124', blank=True, null=True)  # Field name made lowercase.
    vd125 = models.IntegerField(db_column='VD125', blank=True, null=True)  # Field name made lowercase.
    vd126 = models.IntegerField(db_column='VD126', blank=True, null=True)  # Field name made lowercase.
    vd127 = models.IntegerField(db_column='VD127', blank=True, null=True)  # Field name made lowercase.
    vd130 = models.IntegerField(db_column='VD130', blank=True, null=True)  # Field name made lowercase.
    vd131 = models.IntegerField(db_column='VD131', blank=True, null=True)  # Field name made lowercase.
    vd132 = models.IntegerField(db_column='VD132', blank=True, null=True)  # Field name made lowercase.
    vd133 = models.IntegerField(db_column='VD133', blank=True, null=True)  # Field name made lowercase.
    vd134 = models.IntegerField(db_column='VD134', blank=True, null=True)  # Field name made lowercase.
    vd135 = models.IntegerField(db_column='VD135', blank=True, null=True)  # Field name made lowercase.
    vd136 = models.IntegerField(db_column='VD136', blank=True, null=True)  # Field name made lowercase.
    vd137 = models.IntegerField(db_column='VD137', blank=True, null=True)  # Field name made lowercase.
    vd140 = models.IntegerField(db_column='VD140', blank=True, null=True)  # Field name made lowercase.
    vd141 = models.IntegerField(db_column='VD141', blank=True, null=True)  # Field name made lowercase.
    vd142 = models.IntegerField(db_column='VD142', blank=True, null=True)  # Field name made lowercase.
    vd143 = models.IntegerField(db_column='VD143', blank=True, null=True)  # Field name made lowercase.
    vd144 = models.IntegerField(db_column='VD144', blank=True, null=True)  # Field name made lowercase.
    vd145 = models.IntegerField(db_column='VD145', blank=True, null=True)  # Field name made lowercase.
    vd146 = models.IntegerField(db_column='VD146', blank=True, null=True)  # Field name made lowercase.
    vd147 = models.IntegerField(db_column='VD147', blank=True, null=True)  # Field name made lowercase.
    vd150 = models.IntegerField(db_column='VD150', blank=True, null=True)  # Field name made lowercase.
    vd151 = models.IntegerField(db_column='VD151', blank=True, null=True)  # Field name made lowercase.
    vd152 = models.IntegerField(db_column='VD152', blank=True, null=True)  # Field name made lowercase.
    vd153 = models.IntegerField(db_column='VD153', blank=True, null=True)  # Field name made lowercase.
    vd154 = models.IntegerField(db_column='VD154', blank=True, null=True)  # Field name made lowercase.
    vd155 = models.IntegerField(db_column='VD155', blank=True, null=True)  # Field name made lowercase.
    vd156 = models.IntegerField(db_column='VD156', blank=True, null=True)  # Field name made lowercase.
    vd157 = models.IntegerField(db_column='VD157', blank=True, null=True)  # Field name made lowercase.
    vd160 = models.IntegerField(db_column='VD160', blank=True, null=True)  # Field name made lowercase.
    vd161 = models.IntegerField(db_column='VD161', blank=True, null=True)  # Field name made lowercase.
    vd162 = models.IntegerField(db_column='VD162', blank=True, null=True)  # Field name made lowercase.
    vd163 = models.IntegerField(db_column='VD163', blank=True, null=True)  # Field name made lowercase.
    vd164 = models.IntegerField(db_column='VD164', blank=True, null=True)  # Field name made lowercase.
    vd165 = models.IntegerField(db_column='VD165', blank=True, null=True)  # Field name made lowercase.
    vd166 = models.IntegerField(db_column='VD166', blank=True, null=True)  # Field name made lowercase.
    vd167 = models.IntegerField(db_column='VD167', blank=True, null=True)  # Field name made lowercase.
    vd170 = models.IntegerField(db_column='VD170', blank=True, null=True)  # Field name made lowercase.
    vd171 = models.IntegerField(db_column='VD171', blank=True, null=True)  # Field name made lowercase.
    vd172 = models.IntegerField(db_column='VD172', blank=True, null=True)  # Field name made lowercase.
    vd173 = models.IntegerField(db_column='VD173', blank=True, null=True)  # Field name made lowercase.
    vd174 = models.IntegerField(db_column='VD174', blank=True, null=True)  # Field name made lowercase.
    vd175 = models.IntegerField(db_column='VD175', blank=True, null=True)  # Field name made lowercase.
    vd176 = models.IntegerField(db_column='VD176', blank=True, null=True)  # Field name made lowercase.
    vd177 = models.IntegerField(db_column='VD177', blank=True, null=True)  # Field name made lowercase.
    vd200 = models.IntegerField(db_column='VD200', blank=True, null=True)  # Field name made lowercase.
    vd201 = models.IntegerField(db_column='VD201', blank=True, null=True)  # Field name made lowercase.
    vd202 = models.IntegerField(db_column='VD202', blank=True, null=True)  # Field name made lowercase.
    vd203 = models.IntegerField(db_column='VD203', blank=True, null=True)  # Field name made lowercase.
    vd204 = models.IntegerField(db_column='VD204', blank=True, null=True)  # Field name made lowercase.
    vd205 = models.IntegerField(db_column='VD205', blank=True, null=True)  # Field name made lowercase.
    vd206 = models.IntegerField(db_column='VD206', blank=True, null=True)  # Field name made lowercase.
    vd207 = models.IntegerField(db_column='VD207', blank=True, null=True)  # Field name made lowercase.
    vd210 = models.IntegerField(db_column='VD210', blank=True, null=True)  # Field name made lowercase.
    vd211 = models.IntegerField(db_column='VD211', blank=True, null=True)  # Field name made lowercase.
    vd212 = models.IntegerField(db_column='VD212', blank=True, null=True)  # Field name made lowercase.
    vd213 = models.IntegerField(db_column='VD213', blank=True, null=True)  # Field name made lowercase.
    vd214 = models.IntegerField(db_column='VD214', blank=True, null=True)  # Field name made lowercase.
    vd215 = models.IntegerField(db_column='VD215', blank=True, null=True)  # Field name made lowercase.
    vd216 = models.IntegerField(db_column='VD216', blank=True, null=True)  # Field name made lowercase.
    vd217 = models.IntegerField(db_column='VD217', blank=True, null=True)  # Field name made lowercase.
    vd220 = models.IntegerField(db_column='VD220', blank=True, null=True)  # Field name made lowercase.
    vd221 = models.IntegerField(db_column='VD221', blank=True, null=True)  # Field name made lowercase.
    vd222 = models.IntegerField(db_column='VD222', blank=True, null=True)  # Field name made lowercase.
    vd223 = models.IntegerField(db_column='VD223', blank=True, null=True)  # Field name made lowercase.
    vd224 = models.IntegerField(db_column='VD224', blank=True, null=True)  # Field name made lowercase.
    vd225 = models.IntegerField(db_column='VD225', blank=True, null=True)  # Field name made lowercase.
    vd226 = models.IntegerField(db_column='VD226', blank=True, null=True)  # Field name made lowercase.
    vd227 = models.IntegerField(db_column='VD227', blank=True, null=True)  # Field name made lowercase.
    vd230 = models.IntegerField(db_column='VD230', blank=True, null=True)  # Field name made lowercase.
    vd231 = models.IntegerField(db_column='VD231', blank=True, null=True)  # Field name made lowercase.
    vd232 = models.IntegerField(db_column='VD232', blank=True, null=True)  # Field name made lowercase.
    vd233 = models.IntegerField(db_column='VD233', blank=True, null=True)  # Field name made lowercase.
    vd234 = models.IntegerField(db_column='VD234', blank=True, null=True)  # Field name made lowercase.
    vd235 = models.IntegerField(db_column='VD235', blank=True, null=True)  # Field name made lowercase.
    vd236 = models.IntegerField(db_column='VD236', blank=True, null=True)  # Field name made lowercase.
    vd237 = models.IntegerField(db_column='VD237', blank=True, null=True)  # Field name made lowercase.
    vd240 = models.IntegerField(db_column='VD240', blank=True, null=True)  # Field name made lowercase.
    vd241 = models.IntegerField(db_column='VD241', blank=True, null=True)  # Field name made lowercase.
    vd242 = models.IntegerField(db_column='VD242', blank=True, null=True)  # Field name made lowercase.
    vd243 = models.IntegerField(db_column='VD243', blank=True, null=True)  # Field name made lowercase.
    vd244 = models.IntegerField(db_column='VD244', blank=True, null=True)  # Field name made lowercase.
    vd245 = models.IntegerField(db_column='VD245', blank=True, null=True)  # Field name made lowercase.
    vd246 = models.IntegerField(db_column='VD246', blank=True, null=True)  # Field name made lowercase.
    vd247 = models.IntegerField(db_column='VD247', blank=True, null=True)  # Field name made lowercase.
    vd250 = models.IntegerField(db_column='VD250', blank=True, null=True)  # Field name made lowercase.
    vd251 = models.IntegerField(db_column='VD251', blank=True, null=True)  # Field name made lowercase.
    vd252 = models.IntegerField(db_column='VD252', blank=True, null=True)  # Field name made lowercase.
    vd253 = models.IntegerField(db_column='VD253', blank=True, null=True)  # Field name made lowercase.
    vd254 = models.IntegerField(db_column='VD254', blank=True, null=True)  # Field name made lowercase.
    vd255 = models.IntegerField(db_column='VD255', blank=True, null=True)  # Field name made lowercase.
    vd256 = models.IntegerField(db_column='VD256', blank=True, null=True)  # Field name made lowercase.
    vd257 = models.IntegerField(db_column='VD257', blank=True, null=True)  # Field name made lowercase.
    vd260 = models.IntegerField(db_column='VD260', blank=True, null=True)  # Field name made lowercase.
    vd261 = models.IntegerField(db_column='VD261', blank=True, null=True)  # Field name made lowercase.
    vd262 = models.IntegerField(db_column='VD262', blank=True, null=True)  # Field name made lowercase.
    vd263 = models.IntegerField(db_column='VD263', blank=True, null=True)  # Field name made lowercase.
    vd264 = models.IntegerField(db_column='VD264', blank=True, null=True)  # Field name made lowercase.
    vd265 = models.IntegerField(db_column='VD265', blank=True, null=True)  # Field name made lowercase.
    vd266 = models.IntegerField(db_column='VD266', blank=True, null=True)  # Field name made lowercase.
    vd267 = models.IntegerField(db_column='VD267', blank=True, null=True)  # Field name made lowercase.
    vd270 = models.IntegerField(db_column='VD270', blank=True, null=True)  # Field name made lowercase.
    vd271 = models.IntegerField(db_column='VD271', blank=True, null=True)  # Field name made lowercase.
    vd272 = models.IntegerField(db_column='VD272', blank=True, null=True)  # Field name made lowercase.
    vd273 = models.IntegerField(db_column='VD273', blank=True, null=True)  # Field name made lowercase.
    vd274 = models.IntegerField(db_column='VD274', blank=True, null=True)  # Field name made lowercase.
    vd275 = models.IntegerField(db_column='VD275', blank=True, null=True)  # Field name made lowercase.
    vd276 = models.IntegerField(db_column='VD276', blank=True, null=True)  # Field name made lowercase.
    vd277 = models.IntegerField(db_column='VD277', blank=True, null=True)  # Field name made lowercase.
    vd300 = models.IntegerField(db_column='VD300', blank=True, null=True)  # Field name made lowercase.
    vd301 = models.IntegerField(db_column='VD301', blank=True, null=True)  # Field name made lowercase.
    vd302 = models.IntegerField(db_column='VD302', blank=True, null=True)  # Field name made lowercase.
    vd303 = models.IntegerField(db_column='VD303', blank=True, null=True)  # Field name made lowercase.
    vd304 = models.IntegerField(db_column='VD304', blank=True, null=True)  # Field name made lowercase.
    vd305 = models.IntegerField(db_column='VD305', blank=True, null=True)  # Field name made lowercase.
    vd306 = models.IntegerField(db_column='VD306', blank=True, null=True)  # Field name made lowercase.
    vd307 = models.IntegerField(db_column='VD307', blank=True, null=True)  # Field name made lowercase.
    vd310 = models.IntegerField(db_column='VD310', blank=True, null=True)  # Field name made lowercase.
    vd311 = models.IntegerField(db_column='VD311', blank=True, null=True)  # Field name made lowercase.
    vd312 = models.IntegerField(db_column='VD312', blank=True, null=True)  # Field name made lowercase.
    vd313 = models.IntegerField(db_column='VD313', blank=True, null=True)  # Field name made lowercase.
    vd314 = models.IntegerField(db_column='VD314', blank=True, null=True)  # Field name made lowercase.
    vd315 = models.IntegerField(db_column='VD315', blank=True, null=True)  # Field name made lowercase.
    vd316 = models.IntegerField(db_column='VD316', blank=True, null=True)  # Field name made lowercase.
    vd317 = models.IntegerField(db_column='VD317', blank=True, null=True)  # Field name made lowercase.
    vd320 = models.IntegerField(db_column='VD320', blank=True, null=True)  # Field name made lowercase.
    vd321 = models.IntegerField(db_column='VD321', blank=True, null=True)  # Field name made lowercase.
    vd322 = models.IntegerField(db_column='VD322', blank=True, null=True)  # Field name made lowercase.
    vd323 = models.IntegerField(db_column='VD323', blank=True, null=True)  # Field name made lowercase.
    vd324 = models.IntegerField(db_column='VD324', blank=True, null=True)  # Field name made lowercase.
    vd325 = models.IntegerField(db_column='VD325', blank=True, null=True)  # Field name made lowercase.
    vd326 = models.IntegerField(db_column='VD326', blank=True, null=True)  # Field name made lowercase.
    vd327 = models.IntegerField(db_column='VD327', blank=True, null=True)  # Field name made lowercase.
    vd330 = models.IntegerField(db_column='VD330', blank=True, null=True)  # Field name made lowercase.
    vd331 = models.IntegerField(db_column='VD331', blank=True, null=True)  # Field name made lowercase.
    vd332 = models.IntegerField(db_column='VD332', blank=True, null=True)  # Field name made lowercase.
    vd333 = models.IntegerField(db_column='VD333', blank=True, null=True)  # Field name made lowercase.
    vd334 = models.IntegerField(db_column='VD334', blank=True, null=True)  # Field name made lowercase.
    vd335 = models.IntegerField(db_column='VD335', blank=True, null=True)  # Field name made lowercase.
    vd336 = models.IntegerField(db_column='VD336', blank=True, null=True)  # Field name made lowercase.
    vd337 = models.IntegerField(db_column='VD337', blank=True, null=True)  # Field name made lowercase.
    vd340 = models.IntegerField(db_column='VD340', blank=True, null=True)  # Field name made lowercase.
    vd341 = models.IntegerField(db_column='VD341', blank=True, null=True)  # Field name made lowercase.
    vd342 = models.IntegerField(db_column='VD342', blank=True, null=True)  # Field name made lowercase.
    vd343 = models.IntegerField(db_column='VD343', blank=True, null=True)  # Field name made lowercase.
    vd344 = models.IntegerField(db_column='VD344', blank=True, null=True)  # Field name made lowercase.
    vd345 = models.IntegerField(db_column='VD345', blank=True, null=True)  # Field name made lowercase.
    vd346 = models.IntegerField(db_column='VD346', blank=True, null=True)  # Field name made lowercase.
    vd347 = models.IntegerField(db_column='VD347', blank=True, null=True)  # Field name made lowercase.
    vd350 = models.IntegerField(db_column='VD350', blank=True, null=True)  # Field name made lowercase.
    vd351 = models.IntegerField(db_column='VD351', blank=True, null=True)  # Field name made lowercase.
    vd352 = models.IntegerField(db_column='VD352', blank=True, null=True)  # Field name made lowercase.
    vd353 = models.IntegerField(db_column='VD353', blank=True, null=True)  # Field name made lowercase.
    vd354 = models.IntegerField(db_column='VD354', blank=True, null=True)  # Field name made lowercase.
    vd355 = models.IntegerField(db_column='VD355', blank=True, null=True)  # Field name made lowercase.
    vd356 = models.IntegerField(db_column='VD356', blank=True, null=True)  # Field name made lowercase.
    vd357 = models.IntegerField(db_column='VD357', blank=True, null=True)  # Field name made lowercase.
    vd360 = models.IntegerField(db_column='VD360', blank=True, null=True)  # Field name made lowercase.
    vd361 = models.IntegerField(db_column='VD361', blank=True, null=True)  # Field name made lowercase.
    vd362 = models.IntegerField(db_column='VD362', blank=True, null=True)  # Field name made lowercase.
    vd363 = models.IntegerField(db_column='VD363', blank=True, null=True)  # Field name made lowercase.
    vd364 = models.IntegerField(db_column='VD364', blank=True, null=True)  # Field name made lowercase.
    vd365 = models.IntegerField(db_column='VD365', blank=True, null=True)  # Field name made lowercase.
    vd366 = models.IntegerField(db_column='VD366', blank=True, null=True)  # Field name made lowercase.
    vd367 = models.IntegerField(db_column='VD367', blank=True, null=True)  # Field name made lowercase.
    vd370 = models.IntegerField(db_column='VD370', blank=True, null=True)  # Field name made lowercase.
    vd371 = models.IntegerField(db_column='VD371', blank=True, null=True)  # Field name made lowercase.
    vd372 = models.IntegerField(db_column='VD372', blank=True, null=True)  # Field name made lowercase.
    vd373 = models.IntegerField(db_column='VD373', blank=True, null=True)  # Field name made lowercase.
    vd374 = models.IntegerField(db_column='VD374', blank=True, null=True)  # Field name made lowercase.
    vd375 = models.IntegerField(db_column='VD375', blank=True, null=True)  # Field name made lowercase.
    vd376 = models.IntegerField(db_column='VD376', blank=True, null=True)  # Field name made lowercase.
    vd377 = models.IntegerField(db_column='VD377', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'L110KVD_B3'


class L110KInfBlok1(models.Model):
    signals = models.CharField(db_column='SIGNALS', max_length=255, blank=True, primary_key=True)  # Field name made lowercase.
    sig_name = models.CharField(db_column='SIG_NAME', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    sig_def = models.CharField(db_column='SIG_DEF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    koef_1 = models.FloatField(db_column='KOEF_1', blank=True, null=True)  # Field name made lowercase.
    koef_2 = models.FloatField(db_column='KOEF_2', blank=True, null=True)  # Field name made lowercase.
    limits = models.CharField(db_column='LIMITS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'L110K_INF_Blok1'


class L110KInfBlok2(models.Model):
    signals = models.CharField(db_column='SIGNALS', max_length=255, blank=True, primary_key=True)  # Field name made lowercase.
    sig_name = models.CharField(db_column='SIG_NAME', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    sig_def = models.CharField(db_column='SIG_DEF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    koef_1 = models.FloatField(db_column='KOEF_1', blank=True, null=True)  # Field name made lowercase.
    koef_2 = models.FloatField(db_column='KOEF_2', blank=True, null=True)  # Field name made lowercase.
    limits = models.CharField(db_column='LIMITS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'L110K_INF_Blok2'


class L110KInfBlok3(models.Model):
    signals = models.CharField(db_column='SIGNALS', max_length=255, blank=True, primary_key=True)  # Field name made lowercase.
    sig_name = models.CharField(db_column='SIG_NAME', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    sig_def = models.CharField(db_column='SIG_DEF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    koef_1 = models.FloatField(db_column='KOEF_1', blank=True, null=True)  # Field name made lowercase.
    koef_2 = models.FloatField(db_column='KOEF_2', blank=True, null=True)  # Field name made lowercase.
    limits = models.CharField(db_column='LIMITS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'L110K_INF_Blok3'
