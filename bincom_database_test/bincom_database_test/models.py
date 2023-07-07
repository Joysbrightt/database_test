from django.db import models
from django.db import models


class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    state_id = models.IntegerField()

    def __str__(self):
        return str(self.uniqueid)

    # Add other fields as required

# Define other models (Ward, LGA, announced_pu_results, announced_lga_results) in a similar manner
