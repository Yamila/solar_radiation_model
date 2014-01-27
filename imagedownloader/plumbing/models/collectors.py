from django.db import models
from core import Collect
from libs.geometry.jaen import getslots


class CollectTimed(Collect):
	class Meta(object):
		app_label = 'plumbing'
	yearly = models.BooleanField()
	monthly = models.BooleanField()
	weekly = models.BooleanField()
	week_day = models.BooleanField()
	daily = models.BooleanField()
	hourly = models.BooleanField()
	slotly = models.BooleanField()
	slots_by_day = models.IntegerField(default = 1)

	def get_key(self, file_status):
		r = ""
		dt = file_status.material.datetime()
		if self.yearly: r += str(dt.year)
		if self.monthly: r += (".M" + str(dt.month).zfill(2))
		if self.weekly: r += (".W" + str(dt.isocalendar()[1]).zfill(2))
		if self.week_day: r += (".P" + str(dt.weekday()))
		if self.daily: r += (".D" + str(dt.timetuple().tm_yday))
		if self.hourly: r += (".H" + str(dt.hour).zfill(2))
		if self.slotly: r += (".S" + str(getslots(dt.hour,self.slots_by_day/24)).zfill(2))
		return r


class CollectChannel(Collect):
	class Meta(object):
		app_label = 'plumbing'

	def get_key(self, file_status):
		return "BAND_"+str(file_status.material.channel()).zfill(2)