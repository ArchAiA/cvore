from django.db import models

# Create your models here.
class Join(models.Model):
	ref_id = models.CharField(max_length=120, default="ABC", unique=True)
	ip_address = models.CharField(max_length=120)
	email = models.EmailField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return "%s" % (self.email)

	class Meta:
		unique_together = ("email", "ref_id",)