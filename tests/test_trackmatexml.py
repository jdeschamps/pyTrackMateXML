from trackmatexml import trackmatexml

def test_empty_import(empty_xml):
    """Test that TrackmateXML can load an empty xml"""
    assert empty_xml.exists()
    trackmatexml().loadfile(empty_xml)