import pytest

from trackmatexml import TrackmateXML

def test_empty_import(empty_xml):
    """Test that TrackmateXML raise an error for an xml without spots."""
    assert empty_xml.exists()

    # raise error while loading empty xml
    with pytest.raises(ValueError):
        TrackmateXML().loadfile(empty_xml)

def test_twotracks_import(two_tracks_xml):
    """Test that TrackmateXML can read an xml with two tracks."""
    assert two_tracks_xml.exists()

    # load xml
    tmxml = TrackmateXML()
    tmxml.loadfile(two_tracks_xml)

    assert tmxml.tracknames == ['Track_0', 'Track_1']
    assert len(tmxml.spotheader) == 29
    assert tmxml.spots.shape == (4, 29)    
