"""Test suite for the Pink Morsel Sales Visualiser Dash app."""

import pytest
from visualize_data import app


@pytest.fixture
def dash_app():
    """Fixture to provide the Dash app instance."""
    return app


def test_header_is_present(dash_app):
    """Test that the header 'Pink Morsel Sales Visualiser' is present in the layout."""
    layout = dash_app.layout
    
    # Convert layout to string to search for header text
    layout_str = str(layout)
    
    assert 'Pink Morsel Sales Visualiser' in layout_str, "Header text not found in layout"


def test_visualization_is_present(dash_app):
    """Test that the visualization (sales-line-chart Graph) is present in the layout."""
    layout = dash_app.layout
    
    # Search for the Graph component with id 'sales-line-chart'
    layout_str = str(layout)
    
    assert 'sales-line-chart' in layout_str, "Sales line chart component not found in layout"


def test_region_picker_is_present(dash_app):
    """Test that the region picker (RadioItems with id 'region-radio') is present in the layout."""
    layout = dash_app.layout
    
    # Search for the RadioItems component with id 'region-radio'
    layout_str = str(layout)
    
    assert 'region-radio' in layout_str, "Region radio picker component not found in layout"


def test_region_options_are_correct(dash_app):
    """Test that all five region options are present in the region picker."""
    layout = dash_app.layout
    layout_str = str(layout)
    
    regions = ['All', 'North', 'East', 'South', 'West']
    for region in regions:
        assert region in layout_str, f"Region option '{region}' not found in layout"


def test_filter_label_is_present(dash_app):
    """Test that the 'Filter by Region:' label is present."""
    layout = dash_app.layout
    layout_str = str(layout)
    
    assert 'Filter by Region' in layout_str, "Filter label not found in layout"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
