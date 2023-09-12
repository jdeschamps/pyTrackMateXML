from trackmatexml import TrackmateXML

def test_empty_import(empty_xml):
    """Test that TrackmateXML can load an empty xml"""
    assert empty_xml.exists()
    TrackmateXML().loadfile(empty_xml)