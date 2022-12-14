
class PbiHelper:
    def __init__(self, config):
        url = 'https://api.powerbi.cn/v1.0/myorg/'
    
    def get_token(self):
        pass

    def export_to_pdf(self, report_id, group_id, ouput):
        pass

    def refresh_report_in_group(self, group_id, dataset_id):
        interface = 'groups/{group_id}'
