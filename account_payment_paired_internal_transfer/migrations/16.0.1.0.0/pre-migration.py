from openupgradelib import openupgrade

xml_ids = [
    'account_payment_paired_internal_transfer.account_payment_form'
]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xml_id(env, xml_ids)