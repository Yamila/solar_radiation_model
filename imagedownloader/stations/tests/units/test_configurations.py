# -*- coding: utf-8 -*- 
from stations.models import *
from django.test import TestCase
from datetime import datetime
import pytz

class TestConfigurations(TestCase):
	fixtures = [ 'initial_data.yaml', '*']
	
	def setUp(self):
		self.configuration = Configuration.objects.filter(position__station__name = 'Luján')[0]
		#calibration = models.ForeignKey(SensorCalibration)
	
	def test_go_inactive(self):
		# put the end attribute to None to make the configuration
		# active.
		self.configuration.end = None
		self.configuration.save()
		self.assertEqual(self.configuration.end, None)
		# then test that the method go_inactive set the end attribute.
		now = datetime.utcnow().replace(tzinfo=pytz.UTC)
		self.configuration.go_inactive(now)
		self.assertEqual(self.configuration.end, now)

	def test_actives(self):
		# make sure that returns the active configurations set,
		# that mean the configurations without an end attribute.
		are_active = Configuration.actives()
		self.assertTrue(len(are_active) > 0)
		# then if all the active configurations go_inactive, the
		# returned set should have 0 elements.
		for c in are_active:
			c.go_inactive()
		self.assertEqual(len(Configuration.actives()), 0)

	def test_get_backup_filename(self):
		# check if the backup-filename uses the
		# stations/backup/ folder.
		before = datetime.utcnow().replace(microsecond=0)
		filename = self.configuration.get_backup_filename("file.xls")
		after = datetime.utcnow().replace(microsecond=0)
		parts = filename.split(".")
		self.assertEqual(parts[0][:-14], "stations/backup/")
		# then test if the datetime added at the begining of the name use the UTC
		# clock (and check that is between 2 datetime captures).
		dt = datetime.strptime(parts[0][-14:],"%Y%m%d%H%M%S")
		self.assertTrue(before <= dt <= after)
		# finish, test if the original name is at the end of the generated
		# backup-filename. 
		self.assertEqual(filename[-8:], "file.xls")

	"""
        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))
	
    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)"""
