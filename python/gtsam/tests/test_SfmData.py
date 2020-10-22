"""
GTSAM Copyright 2010-2019, Georgia Tech Research Corporation,
Atlanta, Georgia 30332-0415
All Rights Reserved

See LICENSE for the license information

Unit tests for testing dataset access.
Author: Frank Dellaert (Python: Sushmita Warrier)
"""
# pylint: disable=invalid-name, no-name-in-module, no-member

from __future__ import print_function

import unittest

import numpy as np

import gtsam
#from gtsam import SfmCamera
from gtsam.utils.test_case import GtsamTestCase


class TestSfmData(GtsamTestCase):
    """Tests for SfmData and SfmTrack modules."""

    def setUp(self):
        """Initialize SfmData and SfmTrack"""
        self.data = gtsam.SfmData()
        self.tracks = gtsam.SfmTrack()

    def test_tracks(self):
        """Test functions in SfmTrack"""
        # measurement is of format (camera_idx, imgPoint)
        # create camera indices for two cameras
        i1, i2 = np.random.randint(5), np.random.randint(5)
        # create imgPoint for cameras i1 and i2
        uv_i1 = gtsam.Point2(np.random.randint(5), np.random.randint(5))
        uv_i2 = gtsam.Point2(np.random.randint(5), np.random.randint(5))
        m_i1 = (i1, uv_i1)
        m_i2 = (i2, uv_i2)
        # add measurements to the track
        self.tracks.add_measurement(m_i1)
        self.tracks.add_measurement(m_i2)
        # Number of measurements in the track is 2
        self.assertEqual(self.tracks.number_measurements(), 2)
        # camera_idx in the first measurement of the track corresponds to i1
        self.assertEqual(self.tracks.measurement(0)[0], i1)
        # Set arbitrary 3D point corresponding to the track
        self.tracks.setP(gtsam.Point3(2.5, 3.3, 1.2))
        np.testing.assert_array_almost_equal(
            gtsam.Point3(2.5,3.3,1.2), 
            self.tracks.point3()
        )


    def test_data(self):
        """Test functions in SfmData"""
        #cam1 = gtsam.SfmCamera(1500, 1200, 0, 640, 480)
        # Create new track with 3 measurements
        track2 = gtsam.SfmTrack()
        i1, i2, i3 = np.random.randint(5), np.random.randint(5), np.random.randint(5)
        uv_i1 = gtsam.Point2(np.random.randint(5), np.random.randint(5))
        uv_i2 = gtsam.Point2(np.random.randint(5), np.random.randint(5))
        uv_i3 = gtsam.Point2(np.random.randint(5), np.random.randint(5))
        m_i1, m_i2, m_i3 = (i1, uv_i1),  (i2, uv_i2), (i3, uv_i3)
        # add measurements to the track
        track2.add_measurement(m_i1)
        track2.add_measurement(m_i2)
        track2.add_measurement(m_i3)
        self.data.add_track(self.tracks)
        self.data.add_track(track2)
        # Number of tracks in SfmData is 2
        self.assertEqual(self.data.number_tracks(), 2)
        # camera idx of first measurement of second track corresponds to i1
        self.assertEqual(self.data.track(1).measurement(0)[0], i1)

if __name__ == '__main__':
    unittest.main()