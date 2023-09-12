"""
Python reader to convert TrackmateXML to numpy
Version 1.0.0
(c) R.Harkes 2022 NKI

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import json
import os
import logging

import numpy as np
from lxml import etree
from version_parser import Version, VersionType


class TrackmateXML:
    """
    Class to import a TrackmateXML. (c) R.Harkes GPLv3

    Please note that TrackMate is available through Fiji, and is based on a publication.
    If you use it successfully for your research please be so kind to cite the work:
    Tinevez, JY.; Perry, N. & Schindelin, J. et al. (2017), 'TrackMate: An open and extensible platform for single-particle tracking.', Methods 115: 80-90, PMID 27713081.
    https://www.ncbi.nlm.nih.gov/pubmed/27713081
    https://scholar.google.com/scholar?cluster=9846627681021220605
    """

    def __init__(self):
        self.version = None
        self.spatialunits = None
        self.timeunits = None
        self.spotheader = []  # type:[str]
        self.spots = np.zeros((0, 0), dtype=float)
        self.tracks = []  # type: [np.ndarray]
        self.tracknames = []  # type: [str]
        self.displaysettings = {}

    def __bool__(self):
        if self.version:
            return True
        else:
            return False

    def loadfile(self, pth: os.PathLike) -> None:
        """
        Load a TrackMate XML-file
        """
        self._load(etree.parse(pth))

    def loadtree(self, tree: etree.ElementTree) -> None:
        """
        Load a Trackmate XML-tree
        """
        self._load(tree)

    def gettraces(
        self, trackname, spot_property: str, duplicate_split=False, break_split=False
    ) -> list:
        """
        Get traces from a trackname and a spot-property
        """
        tracks = self.analysetrack(trackname, duplicate_split, break_split)
        return [self.getproperty(track["spotids"], spot_property) for track in tracks]

    def getproperty(self, spotids: np.ndarray, spot_property: str) -> np.ndarray:
        """
        Get properties from spotids
        """
        if spot_property not in self.spotheader:
            logging.error(f"{spot_property} not in spot properties")
            return np.zeros((0, 0), dtype=float)
        prop_idx = self.spotheader.index(spot_property)
        spotid_idx = self.spotheader.index("ID")
        res = np.zeros(len(spotids), dtype=np.float)
        for i, s in enumerate(spotids):
            res[i] = self.spots[self.spots[:, spotid_idx] == s, prop_idx]
        return res

    def _load(self, tree) -> None:
        self._getversion(tree.getroot())
        self._analysetree(tree)

    def getversion(self) -> str:
        """
        Get the version of the TrackmateXML data as string.
        """
        return self.version.get_typed_version(VersionType.VERSION)

    def _getversion(self, root) -> None:
        if root.tag == "TrackMate":
            self.version = Version(root.attrib.get("version", None))
            if self.version is None:
                logging.error(f"Invalid Version")
        else:
            logging.error("Not a TrackMateXML")

    def _analysetree(self, tree) -> None:
        root = tree.getroot()
        for element in root:
            if element.tag == "Log":
                self._getlog(element)
            elif element.tag == "Model":
                self._getmodel(element)
            elif element.tag == "Settings":
                self._getsettings(element)
            elif element.tag == "GUIState":
                self._get_gui_state(element)
            elif element.tag == "DisplaySettings":
                self._get_display_settings(element)
            else:
                logging.error(f"Unrecognised element {element}")

    def _getlog(self, element: etree.Element) -> None:
        self.log = element.text

    def _get_display_settings(self, element: etree.Element) -> None:
        self.displaysettings = json.loads(element.text)

    def _getmodel(self, element: etree.Element) -> None:
        self.spatialunits = element.attrib.get("spatialunits", None)
        self.timeunits = element.attrib.get("timeunits", None)
        for subelement in element:
            if subelement.tag == "FeatureDeclarations":
                pass  # would be nice if the feature declaration would actually list the features in the xml, but instead it lists all possible features
            elif subelement.tag == "AllSpots":
                self._getspots(subelement)
            elif subelement.tag == "AllTracks":
                self._gettracks(subelement)
            elif subelement.tag == "FilteredTracks":
                self._getfilteredtracks(subelement)
            else:
                logging.error(f"Unrecognised element {element}")

    def _getsettings(self, element: etree.Element) -> None:
        """
        Could be added, but is not required for displaying intensity tracks
        """
        pass

    def _getfilteredtracks(self, element: etree.Element) -> None:
        """
        Could be added, but is not required for displaying intensity tracks
        """
        pass

    def _get_gui_state(self, element: etree.Element) -> None:
        """
        Could be added, but does not seem usefull in python.
        """
        pass

    def _getspots(self, element: etree.Element) -> None:
        """
        Put all numeric spot data in a numpy array.
        """
        nspots = int(element.attrib.get("nspots", "0"))
        # construct header
        spotid = 0
        spot = element[0][0]
        keys = [a for a in spot.attrib]
        for k in keys:
            try:
                float(spot.attrib[k])
            except ValueError:  # remove keys we cannot convert to floats
                keys.remove(k)
        self.spotheader = keys
        self.spots = np.zeros((nspots, len(keys)))
        for sif in element:
            for spot in sif:
                for i, k in enumerate(keys):
                    self.spots[spotid, i] = spot.attrib.get(k, None)
                spotid += 1

    def _gettracks(self, element: etree.Element) -> None:
        """
        Importing only source and target into a numpy array and listing the trackname.
        We could import more, but it is not needed for displaying intensity tracks.
        """
        for track in element:
            t = np.zeros((len(track), 2), dtype=np.int)
            for i, edge in enumerate(track):
                t[i, 0] = edge.attrib.get("SPOT_SOURCE_ID", -1)
                t[i, 1] = edge.attrib.get("SPOT_TARGET_ID", -1)
            self.tracks.append(t)
            self.tracknames.append(track.attrib.get("name", "unknown"))

    def analysetrack(
        self, trackname: str, duplicate_split=False, break_split=False
    ) -> list:
        """
        Traces a track to find the sequence of spotids
        """
        trackid = self.tracknames.index(trackname)
        return self.analysetrackid(trackid, duplicate_split, break_split)

    def analysetrackid(
        self, trackid: int, duplicate_split=False, break_split=False
    ) -> list:
        """
        Traces a track to find the sequence of spotids
        """
        track = self.tracks[trackid]
        unique_sources = np.setdiff1d(track[:, 0], track[:, 1], assume_unique=True)
        if unique_sources.size != 1:
            logging.error(
                f"Track has {unique_sources.size} startingpoints. Cannot follow track."
            )
            return []
        cellid = 1
        traced_tracks = [
            {
                "parent": 0,
                "cell": cellid,
                "spotids": track[
                    np.argwhere(track[:, 0] == unique_sources), :
                ].flatten(),
                "track": True,
            }
        ]
        while any([x["track"] for x in traced_tracks]):
            for traced_track in traced_tracks:
                if not traced_track["track"]:
                    continue
                traced_track_ids = traced_track["spotids"]
                targetidx = np.argwhere(
                    track[:, 0] == traced_track_ids[-1]
                ).flatten()  # do we find the last index in the sources?
                if targetidx.size == 0:
                    traced_track["track"] = False  # reached the end of the track
                elif targetidx.size == 1:
                    traced_track["spotids"] = np.concatenate(
                        (traced_track_ids, track[targetidx, 1])
                    )  # append target to track
                else:  # multiple targets, a split
                    if duplicate_split:  # a copy of the history is added to each track
                        for i in range(1, targetidx.size):
                            spotids = np.concatenate(
                                (traced_track_ids, [track[targetidx[i], 1]])
                            )
                            cellid += 1
                            new_track = {
                                "parent": traced_track["cell"],
                                "cell": cellid,
                                "spotids": spotids,
                                "track": True,
                            }
                            traced_tracks.append(new_track)
                    else:
                        for i in range(1, targetidx.size):
                            spotids = track[targetidx[i], :]
                            cellid += 1
                            new_track = {
                                "parent": traced_track["cell"],
                                "cell": cellid,
                                "spotids": spotids,
                                "track": True,
                            }
                            traced_tracks.append(new_track)
                    if break_split:
                        traced_track["track"] = False  # end the parent
                        if duplicate_split:
                            spotids = np.concatenate(
                                (traced_track_ids, [track[targetidx[0], 1]])
                            )
                        else:
                            spotids = track[targetidx[0], :]  # start child
                        cellid += 1
                        new_track = {
                            "parent": traced_track["cell"],
                            "cell": cellid,
                            "spotids": spotids,
                            "track": True,
                        }
                        traced_tracks.append(new_track)
                    else:
                        traced_track["spotids"] = np.concatenate(
                            (traced_track_ids, [track[targetidx[0], 1]])
                        )  # append target to track
        return traced_tracks
