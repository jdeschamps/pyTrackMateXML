from pathlib import Path
import pytest


@pytest.fixture
def empty_xml(tmp_path) -> Path:
    # destination path
    path = tmp_path / "Empty.xml"

    # file content corresponding to an empty Trackmate XML file
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <TrackMate version="7.11.1">
    <Log>TrackMate v7.11.1 started on:
    Tue, 12 Sep 2023 10:33:58
    Please note that TrackMate is available through Fiji, and is based on a publication. If you use it successfully for your research please be so kind to cite our work:
    Ershov, D., Phan, MS., Pylvänäinen, J.W., Rigaud S.U., et al. TrackMate 7: integrating state-of-the-art segmentation algorithms into tracking pipelines. Nat Methods (2022). https://doi.org/10.1038/s41592-022-01507-1
    https://doi.org/10.1038/s41592-022-01507-1
    and / or:
    Tinevez, JY.; Perry, N. &amp; Schindelin, J. et al. (2017), 'TrackMate: An open and extensible platform for single-particle tracking.', Methods 115: 80-90, PMID 27713081.
    https://www.sciencedirect.com/science/article/pii/S1046202316303346

    Numerical feature analyzers:
    Spot feature analyzers:
    - Manual spot color provides: Spot color; is manual.
    - Spot intensity provides: Mean ch1, Median ch1, Min ch1, Max ch1, Sum ch1, Std ch1.
    - ExTrack probabilities provides: P stuck, P diffusive; is manual.
    - Spot contrast and SNR provides: Ctrst ch1, SNR ch1.
    Edge feature analyzers:
    - Directional change provides: γ rate.
    - Edge speed provides: Speed, Disp.
    - Edge target provides: Source ID, Target ID, Cost.
    - Edge location provides: Edge T, Edge X, Edge Y, Edge Z.
    - Manual edge color provides: Edge color; is manual.
    Track feature analyzers:
    - Branching analyzer provides: N spots, N gaps, N splits, N merges, N complex, Lgst gap.
    - Track duration provides: Duration, Track start, Track stop, Track disp.
    - Track index provides: Index, ID.
    - Track location provides: Track X, Track Y, Track Z.
    - Track speed provides: Mean sp., Max speed, Min speed, Med. speed, Std speed.
    - Track quality provides: Mean Q.
    - Track motility analysis provides: Total dist., Max dist., Cfn. ratio, Mn. v. line, Fwd. progr., Mn. γ rate.

    Image region of interest:
    Image data:
    For the image named: Example.
    Matching file Example in current folder.
    Geometry:
    X =    0 -  511, dx = 1.00000
    Y =    0 -  511, dy = 1.00000
    Z =    0 -    0, dz = 1.00000
    T =    0 -    1, dt = 1.00000

    Configured detector LoG detector with settings:
    - target channel: 1
    - threshold: 0.8
    - do median filtering: false
    - radius: 5.0
    - do subpixel localization: true

    Starting detection process using 16 threads.
    Detection processes 2 frames simultaneously and allocates 8 threads per frame.
    Found 0 spots.
    Detection done in 0.2 s.

    Computing spot quality histogram...
    Initial thresholding with a quality threshold above 0.2 ...
    Starting initial filtering process.
    Retained 0 spots out of 0.

    Calculating spot features...
    Calculating features done in 0.0 s.

    Performing spot filtering on the following features:
    No feature threshold set, kept the 0 spots.

    Configured tracker Simple LAP tracker with settings:
    - max frame gap: 2
    - alternative linking cost factor: 1.05
    - linking feature penalties: 
    - linking max distance: 15.0
    - gap closing max distance: 15.0
    - merging feature penalties: 
    - splitting max distance: 15.0
    - blocking value: Infinity
    - allow gap closing: true
    - allow track splitting: false
    - allow track merging: false
    - merging max distance: 15.0
    - splitting feature penalties: 
    - cutoff percentile: 0.9
    - gap closing feature penalties: 

    Starting tracking process.
    Tracking done in 0.0 s.
    Found 0 tracks.
    - avg size: 0.0 spots.
    - min size: 2147483647 spots.
    - max size: -2147483648 spots.

    Calculating features done in 0.0 s.
    Saving data...
    Warning: The source image does not match a file on the system.TrackMate won't be able to reload it when opening this XML file.
    To fix this, save the source image to a TIF file before saving the TrackMate session.</Log>
    <Model spatialunits="pixel" timeunits="frame">
        <FeatureDeclarations>
        <SpotFeatures>
            <Feature feature="QUALITY" name="Quality" shortname="Quality" dimension="QUALITY" isint="false" />
            <Feature feature="POSITION_X" name="X" shortname="X" dimension="POSITION" isint="false" />
            <Feature feature="POSITION_Y" name="Y" shortname="Y" dimension="POSITION" isint="false" />
            <Feature feature="POSITION_Z" name="Z" shortname="Z" dimension="POSITION" isint="false" />
            <Feature feature="POSITION_T" name="T" shortname="T" dimension="TIME" isint="false" />
            <Feature feature="FRAME" name="Frame" shortname="Frame" dimension="NONE" isint="true" />
            <Feature feature="RADIUS" name="Radius" shortname="R" dimension="LENGTH" isint="false" />
            <Feature feature="VISIBILITY" name="Visibility" shortname="Visibility" dimension="NONE" isint="true" />
            <Feature feature="MANUAL_SPOT_COLOR" name="Manual spot color" shortname="Spot color" dimension="NONE" isint="true" />
            <Feature feature="MEAN_INTENSITY_CH1" name="Mean intensity ch1" shortname="Mean ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="MEDIAN_INTENSITY_CH1" name="Median intensity ch1" shortname="Median ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="MIN_INTENSITY_CH1" name="Min intensity ch1" shortname="Min ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="MAX_INTENSITY_CH1" name="Max intensity ch1" shortname="Max ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="TOTAL_INTENSITY_CH1" name="Sum intensity ch1" shortname="Sum ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="STD_INTENSITY_CH1" name="Std intensity ch1" shortname="Std ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="EXTRACK_P_STUCK" name="Probability stuck" shortname="P stuck" dimension="NONE" isint="false" />
            <Feature feature="EXTRACK_P_DIFFUSIVE" name="Probability diffusive" shortname="P diffusive" dimension="NONE" isint="false" />
            <Feature feature="CONTRAST_CH1" name="Contrast ch1" shortname="Ctrst ch1" dimension="NONE" isint="false" />
            <Feature feature="SNR_CH1" name="Signal/Noise ratio ch1" shortname="SNR ch1" dimension="NONE" isint="false" />
        </SpotFeatures>
        <EdgeFeatures>
            <Feature feature="SPOT_SOURCE_ID" name="Source spot ID" shortname="Source ID" dimension="NONE" isint="true" />
            <Feature feature="SPOT_TARGET_ID" name="Target spot ID" shortname="Target ID" dimension="NONE" isint="true" />
            <Feature feature="LINK_COST" name="Edge cost" shortname="Cost" dimension="COST" isint="false" />
            <Feature feature="DIRECTIONAL_CHANGE_RATE" name="Directional change rate" shortname="γ rate" dimension="ANGLE_RATE" isint="false" />
            <Feature feature="SPEED" name="Speed" shortname="Speed" dimension="VELOCITY" isint="false" />
            <Feature feature="DISPLACEMENT" name="Displacement" shortname="Disp." dimension="LENGTH" isint="false" />
            <Feature feature="EDGE_TIME" name="Edge time" shortname="Edge T" dimension="TIME" isint="false" />
            <Feature feature="EDGE_X_LOCATION" name="Edge X" shortname="Edge X" dimension="POSITION" isint="false" />
            <Feature feature="EDGE_Y_LOCATION" name="Edge Y" shortname="Edge Y" dimension="POSITION" isint="false" />
            <Feature feature="EDGE_Z_LOCATION" name="Edge Z" shortname="Edge Z" dimension="POSITION" isint="false" />
            <Feature feature="MANUAL_EDGE_COLOR" name="Manual edge color" shortname="Edge color" dimension="NONE" isint="true" />
        </EdgeFeatures>
        <TrackFeatures>
            <Feature feature="TRACK_INDEX" name="Track index" shortname="Index" dimension="NONE" isint="true" />
            <Feature feature="TRACK_ID" name="Track ID" shortname="ID" dimension="NONE" isint="true" />
            <Feature feature="NUMBER_SPOTS" name="Number of spots in track" shortname="N spots" dimension="NONE" isint="true" />
            <Feature feature="NUMBER_GAPS" name="Number of gaps" shortname="N gaps" dimension="NONE" isint="true" />
            <Feature feature="NUMBER_SPLITS" name="Number of split events" shortname="N splits" dimension="NONE" isint="true" />
            <Feature feature="NUMBER_MERGES" name="Number of merge events" shortname="N merges" dimension="NONE" isint="true" />
            <Feature feature="NUMBER_COMPLEX" name="Number of complex points" shortname="N complex" dimension="NONE" isint="true" />
            <Feature feature="LONGEST_GAP" name="Longest gap" shortname="Lgst gap" dimension="NONE" isint="true" />
            <Feature feature="TRACK_DURATION" name="Track duration" shortname="Duration" dimension="TIME" isint="false" />
            <Feature feature="TRACK_START" name="Track start" shortname="Track start" dimension="TIME" isint="false" />
            <Feature feature="TRACK_STOP" name="Track stop" shortname="Track stop" dimension="TIME" isint="false" />
            <Feature feature="TRACK_DISPLACEMENT" name="Track displacement" shortname="Track disp." dimension="LENGTH" isint="false" />
            <Feature feature="TRACK_X_LOCATION" name="Track mean X" shortname="Track X" dimension="POSITION" isint="false" />
            <Feature feature="TRACK_Y_LOCATION" name="Track mean Y" shortname="Track Y" dimension="POSITION" isint="false" />
            <Feature feature="TRACK_Z_LOCATION" name="Track mean Z" shortname="Track Z" dimension="POSITION" isint="false" />
            <Feature feature="TRACK_MEAN_SPEED" name="Track mean speed" shortname="Mean sp." dimension="VELOCITY" isint="false" />
            <Feature feature="TRACK_MAX_SPEED" name="Track max speed" shortname="Max speed" dimension="VELOCITY" isint="false" />
            <Feature feature="TRACK_MIN_SPEED" name="Track min speed" shortname="Min speed" dimension="VELOCITY" isint="false" />
            <Feature feature="TRACK_MEDIAN_SPEED" name="Track median speed" shortname="Med. speed" dimension="VELOCITY" isint="false" />
            <Feature feature="TRACK_STD_SPEED" name="Track std speed" shortname="Std speed" dimension="VELOCITY" isint="false" />
            <Feature feature="TRACK_MEAN_QUALITY" name="Track mean quality" shortname="Mean Q" dimension="QUALITY" isint="false" />
            <Feature feature="TOTAL_DISTANCE_TRAVELED" name="Total distance traveled" shortname="Total dist." dimension="LENGTH" isint="false" />
            <Feature feature="MAX_DISTANCE_TRAVELED" name="Max distance traveled" shortname="Max dist." dimension="LENGTH" isint="false" />
            <Feature feature="CONFINEMENT_RATIO" name="Confinement ratio" shortname="Cfn. ratio" dimension="NONE" isint="false" />
            <Feature feature="MEAN_STRAIGHT_LINE_SPEED" name="Mean straight line speed" shortname="Mn. v. line" dimension="VELOCITY" isint="false" />
            <Feature feature="LINEARITY_OF_FORWARD_PROGRESSION" name="Linearity of forward progression" shortname="Fwd. progr." dimension="NONE" isint="false" />
            <Feature feature="MEAN_DIRECTIONAL_CHANGE_RATE" name="Mean directional change rate" shortname="Mn. γ rate" dimension="ANGLE_RATE" isint="false" />
        </TrackFeatures>
        </FeatureDeclarations>
        <AllSpots nspots="0">
        <SpotsInFrame frame="0" />
        <SpotsInFrame frame="1" />
        </AllSpots>
        <AllTracks />
        <FilteredTracks />
    </Model>
    <Settings>
        <ImageData filename="Example" folder="" width="512" height="512" nslices="1" nframes="2" pixelwidth="1.0" pixelheight="1.0" voxeldepth="1.0" timeinterval="1.0" />
        <BasicSettings xstart="0" xend="511" ystart="0" yend="511" zstart="0" zend="0" tstart="0" tend="1" />
        <DetectorSettings DETECTOR_NAME="LOG_DETECTOR" TARGET_CHANNEL="1" RADIUS="5.0" THRESHOLD="0.8" DO_MEDIAN_FILTERING="false" DO_SUBPIXEL_LOCALIZATION="true" />
        <InitialSpotFilter feature="QUALITY" value="0.22185452133476247" isabove="true" />
        <SpotFilterCollection />
        <TrackerSettings TRACKER_NAME="SIMPLE_SPARSE_LAP_TRACKER" CUTOFF_PERCENTILE="0.9" ALTERNATIVE_LINKING_COST_FACTOR="1.05" BLOCKING_VALUE="Infinity">
        <Linking LINKING_MAX_DISTANCE="15.0">
            <FeaturePenalties />
        </Linking>
        <GapClosing ALLOW_GAP_CLOSING="true" GAP_CLOSING_MAX_DISTANCE="15.0" MAX_FRAME_GAP="2">
            <FeaturePenalties />
        </GapClosing>
        <TrackSplitting ALLOW_TRACK_SPLITTING="false" SPLITTING_MAX_DISTANCE="15.0">
            <FeaturePenalties />
        </TrackSplitting>
        <TrackMerging ALLOW_TRACK_MERGING="false" MERGING_MAX_DISTANCE="15.0">
            <FeaturePenalties />
        </TrackMerging>
        </TrackerSettings>
        <TrackFilterCollection />
        <AnalyzerCollection>
        <SpotAnalyzers>
            <Analyzer key="Manual spot color" />
            <Analyzer key="Spot intensity" />
            <Analyzer key="EXTRACK_PROBABILITIES" />
            <Analyzer key="Spot contrast and SNR" />
        </SpotAnalyzers>
        <EdgeAnalyzers>
            <Analyzer key="Directional change" />
            <Analyzer key="Edge speed" />
            <Analyzer key="Edge target" />
            <Analyzer key="Edge location" />
            <Analyzer key="Manual edge color" />
        </EdgeAnalyzers>
        <TrackAnalyzers>
            <Analyzer key="Branching analyzer" />
            <Analyzer key="Track duration" />
            <Analyzer key="Track index" />
            <Analyzer key="Track location" />
            <Analyzer key="Track speed" />
            <Analyzer key="Track quality" />
            <Analyzer key="Track motility analysis" />
        </TrackAnalyzers>
        </AnalyzerCollection>
    </Settings>
    <GUIState state="TrackFilter" />
    <DisplaySettings>{
    "name": "CurrentDisplaySettings",
    "spotUniformColor": "204, 51, 204, 255",
    "spotColorByType": "DEFAULT",
    "spotColorByFeature": "UNIFORM_COLOR",
    "spotDisplayRadius": 1.0,
    "spotDisplayedAsRoi": true,
    "spotMin": 0.0,
    "spotMax": 10.0,
    "spotShowName": false,
    "trackMin": 0.0,
    "trackMax": 10.0,
    "trackColorByType": "TRACKS",
    "trackColorByFeature": "TRACK_INDEX",
    "trackUniformColor": "204, 204, 51, 255",
    "undefinedValueColor": "0, 0, 0, 255",
    "missingValueColor": "89, 89, 89, 255",
    "highlightColor": "51, 230, 51, 255",
    "trackDisplayMode": "FULL",
    "colormap": "Jet",
    "limitZDrawingDepth": false,
    "drawingZDepth": 10.0,
    "fadeTracks": true,
    "fadeTrackRange": 30,
    "useAntialiasing": true,
    "spotVisible": true,
    "trackVisible": true,
    "font": {
        "name": "Arial",
        "style": 1,
        "size": 12,
        "pointSize": 12.0,
        "fontSerializedDataVersion": 1
    },
    "lineThickness": 1.0,
    "selectionLineThickness": 4.0,
    "trackschemeBackgroundColor1": "128, 128, 128, 255",
    "trackschemeBackgroundColor2": "192, 192, 192, 255",
    "trackschemeForegroundColor": "0, 0, 0, 255",
    "trackschemeDecorationColor": "0, 0, 0, 255",
    "trackschemeFillBox": false,
    "spotFilled": false,
    "spotTransparencyAlpha": 1.0
    }</DisplaySettings>
    </TrackMate>'''

    # write file
    with open(path, "w") as f:
        f.write(xml)

    return path


@pytest.fixture
def two_tracks_xml(tmp_path) -> Path:
    # destination path
    path = tmp_path / "TwoTracks.xml"

    # file content corresponding to an empty Trackmate XML file
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <TrackMate version="7.11.1">
    <Log>TrackMate v7.11.1 started on:
    Tue, 12 Sep 2023 11:42:16
    Please note that TrackMate is available through Fiji, and is based on a publication. If you use it successfully for your research please be so kind to cite our work:
    Ershov, D., Phan, MS., Pylvänäinen, J.W., Rigaud S.U., et al. TrackMate 7: integrating state-of-the-art segmentation algorithms into tracking pipelines. Nat Methods (2022). https://doi.org/10.1038/s41592-022-01507-1
    https://doi.org/10.1038/s41592-022-01507-1
    and / or:
    Tinevez, JY.; Perry, N. &amp; Schindelin, J. et al. (2017), 'TrackMate: An open and extensible platform for single-particle tracking.', Methods 115: 80-90, PMID 27713081.
    https://www.sciencedirect.com/science/article/pii/S1046202316303346

    Numerical feature analyzers:
    Spot feature analyzers:
    - Manual spot color provides: Spot color; is manual.
    - Spot intensity provides: Mean ch1, Median ch1, Min ch1, Max ch1, Sum ch1, Std ch1.
    - ExTrack probabilities provides: P stuck, P diffusive; is manual.
    - Spot contrast and SNR provides: Ctrst ch1, SNR ch1.
    Edge feature analyzers:
    - Directional change provides: γ rate.
    - Edge speed provides: Speed, Disp.
    - Edge target provides: Source ID, Target ID, Cost.
    - Edge location provides: Edge T, Edge X, Edge Y, Edge Z.
    - Manual edge color provides: Edge color; is manual.
    Track feature analyzers:
    - Branching analyzer provides: N spots, N gaps, N splits, N merges, N complex, Lgst gap.
    - Track duration provides: Duration, Track start, Track stop, Track disp.
    - Track index provides: Index, ID.
    - Track location provides: Track X, Track Y, Track Z.
    - Track speed provides: Mean sp., Max speed, Min speed, Med. speed, Std speed.
    - Track quality provides: Mean Q.
    - Track motility analysis provides: Total dist., Max dist., Cfn. ratio, Mn. v. line, Fwd. progr., Mn. γ rate.

    Image region of interest:
    Image data:
    For the image named: Untitled.
    Matching file Untitled in current folder.
    Geometry:
    X =    0 -  511, dx = 1.00000
    Y =    0 -  511, dy = 1.00000
    Z =    0 -    0, dz = 1.00000
    T =    0 -    1, dt = 1.00000

    Configured detector LoG detector with settings:
    - target channel: 1
    - threshold: 2.548415005980352
    - do median filtering: false
    - radius: 17.0
    - do subpixel localization: true

    Initial thresholding with a quality threshold above 0.2 ...
    Starting initial filtering process.
    Retained 0 spots out of 0.

    Adding morphology analyzers...
    - Spot fit 2D ellipse provides: El. x0, El. y0, El. long axis, El. sh. axis, El. angle, El. a.r.
    - Spot 2D shape descriptors provides: Area, Perim., Circ., Solidity, Shape index.

    Calculating spot features...
    Calculating features done in 0.0 s.

    Performing spot filtering on the following features:
    No feature threshold set, kept the 0 spots.

    Configured detector Thresholding detector with settings:
    - target channel: 1
    - simplify contours: true
    - intensity threshold: 254.0

    Starting detection process using 16 threads.
    Detection processes 2 frames simultaneously and allocates 8 threads per frame.
    Found 4 spots.
    Detection done in 0.1 s.

    Computing spot quality histogram...
    Initial thresholding with a quality threshold above 0.2 ...
    Starting initial filtering process.
    Retained 4 spots out of 4.

    Adding morphology analyzers...
    - Spot fit 2D ellipse provides: El. x0, El. y0, El. long axis, El. sh. axis, El. angle, El. a.r.
    - Spot 2D shape descriptors provides: Area, Perim., Circ., Solidity, Shape index.

    Calculating spot features...
    Calculating features done in 0.0 s.

    Performing spot filtering on the following features:
    No feature threshold set, kept the 4 spots.

    Configured tracker Simple LAP tracker with settings:
    - max frame gap: 2
    - alternative linking cost factor: 1.05
    - linking feature penalties: 
    - linking max distance: 15.0
    - gap closing max distance: 15.0
    - merging feature penalties: 
    - splitting max distance: 15.0
    - blocking value: Infinity
    - allow gap closing: true
    - allow track splitting: false
    - allow track merging: false
    - merging max distance: 15.0
    - splitting feature penalties: 
    - cutoff percentile: 0.9
    - gap closing feature penalties: 

    Starting tracking process.
    Tracking done in 0.0 s.
    Found 2 tracks.
    - avg size: 2.0 spots.
    - min size: 2 spots.
    - max size: 2 spots.

    Calculating features done in 0.0 s.

    Performing track filtering on the following features:
    No feature threshold set, kept the 2 tracks.
    Saving data...
    Warning: The source image does not match a file on the system.TrackMate won't be able to reload it when opening this XML file.
    To fix this, save the source image to a TIF file before saving the TrackMate session.
    Computing edge features:
    - Directional change in 1 ms.
    - Edge speed in 0 ms.
    - Edge target in 1 ms.
    - Edge location in 0 ms.
    Computation done in 2 ms.
    Computing track features:
    - Branching analyzer in 0 ms.
    - Track duration in 1 ms.
    - Track index in 0 ms.
    - Track location in 0 ms.
    - Track speed in 0 ms.
    - Track quality in 0 ms.
    - Track motility analysis in 1 ms.
    Computation done in 2 ms.
    Added log.
    Added spot, edge and track feature declarations.
    Added 4 spots.
    Added tracks.
    Added filtered tracks.
    Added image information.
    Added crop settings.
    Added detector settings.
    Added initial spot filter.
    Added spot feature filters.
    Added tracker settings.
    Added track feature filters.
    Added spot, edge and track analyzers.
    Added GUI current state.
    Added display settings.
    Writing to file.
    Data saved to: /Applications/Fiji.app/Untitled.xml
    Saving data...
    Warning: The source image does not match a file on the system.TrackMate won't be able to reload it when opening this XML file.
    To fix this, save the source image to a TIF file before saving the TrackMate session.
    Computing edge features:
    - Directional change in 0 ms.
    - Edge speed in 0 ms.
    - Edge target in 1 ms.
    - Edge location in 0 ms.
    Computation done in 1 ms.
    Computing track features:
    - Branching analyzer in 1 ms.
    - Track duration in 0 ms.
    - Track index in 0 ms.
    - Track location in 0 ms.
    - Track speed in 0 ms.
    - Track quality in 0 ms.
    - Track motility analysis in 0 ms.
    Computation done in 2 ms.</Log>
    <Model spatialunits="pixel" timeunits="frame">
        <FeatureDeclarations>
        <SpotFeatures>
            <Feature feature="QUALITY" name="Quality" shortname="Quality" dimension="QUALITY" isint="false" />
            <Feature feature="POSITION_X" name="X" shortname="X" dimension="POSITION" isint="false" />
            <Feature feature="POSITION_Y" name="Y" shortname="Y" dimension="POSITION" isint="false" />
            <Feature feature="POSITION_Z" name="Z" shortname="Z" dimension="POSITION" isint="false" />
            <Feature feature="POSITION_T" name="T" shortname="T" dimension="TIME" isint="false" />
            <Feature feature="FRAME" name="Frame" shortname="Frame" dimension="NONE" isint="true" />
            <Feature feature="RADIUS" name="Radius" shortname="R" dimension="LENGTH" isint="false" />
            <Feature feature="VISIBILITY" name="Visibility" shortname="Visibility" dimension="NONE" isint="true" />
            <Feature feature="MANUAL_SPOT_COLOR" name="Manual spot color" shortname="Spot color" dimension="NONE" isint="true" />
            <Feature feature="MEAN_INTENSITY_CH1" name="Mean intensity ch1" shortname="Mean ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="MEDIAN_INTENSITY_CH1" name="Median intensity ch1" shortname="Median ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="MIN_INTENSITY_CH1" name="Min intensity ch1" shortname="Min ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="MAX_INTENSITY_CH1" name="Max intensity ch1" shortname="Max ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="TOTAL_INTENSITY_CH1" name="Sum intensity ch1" shortname="Sum ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="STD_INTENSITY_CH1" name="Std intensity ch1" shortname="Std ch1" dimension="INTENSITY" isint="false" />
            <Feature feature="EXTRACK_P_STUCK" name="Probability stuck" shortname="P stuck" dimension="NONE" isint="false" />
            <Feature feature="EXTRACK_P_DIFFUSIVE" name="Probability diffusive" shortname="P diffusive" dimension="NONE" isint="false" />
            <Feature feature="CONTRAST_CH1" name="Contrast ch1" shortname="Ctrst ch1" dimension="NONE" isint="false" />
            <Feature feature="SNR_CH1" name="Signal/Noise ratio ch1" shortname="SNR ch1" dimension="NONE" isint="false" />
            <Feature feature="ELLIPSE_X0" name="Ellipse center x0" shortname="El. x0" dimension="LENGTH" isint="false" />
            <Feature feature="ELLIPSE_Y0" name="Ellipse center y0" shortname="El. y0" dimension="LENGTH" isint="false" />
            <Feature feature="ELLIPSE_MAJOR" name="Ellipse long axis" shortname="El. long axis" dimension="LENGTH" isint="false" />
            <Feature feature="ELLIPSE_MINOR" name="Ellipse short axis" shortname="El. sh. axis" dimension="LENGTH" isint="false" />
            <Feature feature="ELLIPSE_THETA" name="Ellipse angle" shortname="El. angle" dimension="ANGLE" isint="false" />
            <Feature feature="ELLIPSE_ASPECTRATIO" name="Ellipse aspect ratio" shortname="El. a.r." dimension="NONE" isint="false" />
            <Feature feature="AREA" name="Area" shortname="Area" dimension="AREA" isint="false" />
            <Feature feature="PERIMETER" name="Perimeter" shortname="Perim." dimension="LENGTH" isint="false" />
            <Feature feature="CIRCULARITY" name="Circularity" shortname="Circ." dimension="NONE" isint="false" />
            <Feature feature="SOLIDITY" name="Solidity" shortname="Solidity" dimension="NONE" isint="false" />
            <Feature feature="SHAPE_INDEX" name="Shape index" shortname="Shape index" dimension="NONE" isint="false" />
        </SpotFeatures>
        <EdgeFeatures>
            <Feature feature="SPOT_SOURCE_ID" name="Source spot ID" shortname="Source ID" dimension="NONE" isint="true" />
            <Feature feature="SPOT_TARGET_ID" name="Target spot ID" shortname="Target ID" dimension="NONE" isint="true" />
            <Feature feature="LINK_COST" name="Edge cost" shortname="Cost" dimension="COST" isint="false" />
            <Feature feature="DIRECTIONAL_CHANGE_RATE" name="Directional change rate" shortname="γ rate" dimension="ANGLE_RATE" isint="false" />
            <Feature feature="SPEED" name="Speed" shortname="Speed" dimension="VELOCITY" isint="false" />
            <Feature feature="DISPLACEMENT" name="Displacement" shortname="Disp." dimension="LENGTH" isint="false" />
            <Feature feature="EDGE_TIME" name="Edge time" shortname="Edge T" dimension="TIME" isint="false" />
            <Feature feature="EDGE_X_LOCATION" name="Edge X" shortname="Edge X" dimension="POSITION" isint="false" />
            <Feature feature="EDGE_Y_LOCATION" name="Edge Y" shortname="Edge Y" dimension="POSITION" isint="false" />
            <Feature feature="EDGE_Z_LOCATION" name="Edge Z" shortname="Edge Z" dimension="POSITION" isint="false" />
            <Feature feature="MANUAL_EDGE_COLOR" name="Manual edge color" shortname="Edge color" dimension="NONE" isint="true" />
        </EdgeFeatures>
        <TrackFeatures>
            <Feature feature="TRACK_INDEX" name="Track index" shortname="Index" dimension="NONE" isint="true" />
            <Feature feature="TRACK_ID" name="Track ID" shortname="ID" dimension="NONE" isint="true" />
            <Feature feature="NUMBER_SPOTS" name="Number of spots in track" shortname="N spots" dimension="NONE" isint="true" />
            <Feature feature="NUMBER_GAPS" name="Number of gaps" shortname="N gaps" dimension="NONE" isint="true" />
            <Feature feature="NUMBER_SPLITS" name="Number of split events" shortname="N splits" dimension="NONE" isint="true" />
            <Feature feature="NUMBER_MERGES" name="Number of merge events" shortname="N merges" dimension="NONE" isint="true" />
            <Feature feature="NUMBER_COMPLEX" name="Number of complex points" shortname="N complex" dimension="NONE" isint="true" />
            <Feature feature="LONGEST_GAP" name="Longest gap" shortname="Lgst gap" dimension="NONE" isint="true" />
            <Feature feature="TRACK_DURATION" name="Track duration" shortname="Duration" dimension="TIME" isint="false" />
            <Feature feature="TRACK_START" name="Track start" shortname="Track start" dimension="TIME" isint="false" />
            <Feature feature="TRACK_STOP" name="Track stop" shortname="Track stop" dimension="TIME" isint="false" />
            <Feature feature="TRACK_DISPLACEMENT" name="Track displacement" shortname="Track disp." dimension="LENGTH" isint="false" />
            <Feature feature="TRACK_X_LOCATION" name="Track mean X" shortname="Track X" dimension="POSITION" isint="false" />
            <Feature feature="TRACK_Y_LOCATION" name="Track mean Y" shortname="Track Y" dimension="POSITION" isint="false" />
            <Feature feature="TRACK_Z_LOCATION" name="Track mean Z" shortname="Track Z" dimension="POSITION" isint="false" />
            <Feature feature="TRACK_MEAN_SPEED" name="Track mean speed" shortname="Mean sp." dimension="VELOCITY" isint="false" />
            <Feature feature="TRACK_MAX_SPEED" name="Track max speed" shortname="Max speed" dimension="VELOCITY" isint="false" />
            <Feature feature="TRACK_MIN_SPEED" name="Track min speed" shortname="Min speed" dimension="VELOCITY" isint="false" />
            <Feature feature="TRACK_MEDIAN_SPEED" name="Track median speed" shortname="Med. speed" dimension="VELOCITY" isint="false" />
            <Feature feature="TRACK_STD_SPEED" name="Track std speed" shortname="Std speed" dimension="VELOCITY" isint="false" />
            <Feature feature="TRACK_MEAN_QUALITY" name="Track mean quality" shortname="Mean Q" dimension="QUALITY" isint="false" />
            <Feature feature="TOTAL_DISTANCE_TRAVELED" name="Total distance traveled" shortname="Total dist." dimension="LENGTH" isint="false" />
            <Feature feature="MAX_DISTANCE_TRAVELED" name="Max distance traveled" shortname="Max dist." dimension="LENGTH" isint="false" />
            <Feature feature="CONFINEMENT_RATIO" name="Confinement ratio" shortname="Cfn. ratio" dimension="NONE" isint="false" />
            <Feature feature="MEAN_STRAIGHT_LINE_SPEED" name="Mean straight line speed" shortname="Mn. v. line" dimension="VELOCITY" isint="false" />
            <Feature feature="LINEARITY_OF_FORWARD_PROGRESSION" name="Linearity of forward progression" shortname="Fwd. progr." dimension="NONE" isint="false" />
            <Feature feature="MEAN_DIRECTIONAL_CHANGE_RATE" name="Mean directional change rate" shortname="Mn. γ rate" dimension="ANGLE_RATE" isint="false" />
        </TrackFeatures>
        </FeatureDeclarations>
        <AllSpots nspots="4">
        <SpotsInFrame frame="0">
            <Spot ID="336316" name="ID336316" STD_INTENSITY_CH1="22.26675252697455" SOLIDITY="0.9822389666307861" QUALITY="910.0" POSITION_T="0.0" TOTAL_INTENSITY_CH1="230775.0" CONTRAST_CH1="0.9948595339882516" ELLIPSE_MINOR="17.026195350916595" ELLIPSE_THETA="1.3057152350530556" ELLIPSE_Y0="0.06124908722332005" FRAME="0" CIRCULARITY="0.936399053148603" AREA="912.5000000000001" ELLIPSE_MAJOR="17.21789122806879" MEAN_INTENSITY_CH1="253.04276315789474" MAX_INTENSITY_CH1="255.0" MIN_INTENSITY_CH1="0.0" SNR_CH1="11.334868344974025" ELLIPSE_X0="0.002593896438477291" SHAPE_INDEX="3.6633165589713275" MEDIAN_INTENSITY_CH1="255.0" VISIBILITY="1" RADIUS="17.042821689576787" POSITION_X="157.50748858447488" POSITION_Y="141.43315068493152" ELLIPSE_ASPECTRATIO="1.0112588792270538" POSITION_Z="0.0" PERIMETER="110.66005599470205" ROI_N_POINTS="36">3.992511415525115 17.06684931506848 10.992511415525115 13.066849315068481 12.992511415525115 12.066849315068481 12.992511415525115 10.066849315068481 14.992511415525115 9.066849315068481 15.992511415525115 5.066849315068481 16.992511415525115 4.066849315068481 16.992511415525115 0.06684931506848102 16.992511415525115 -1.933150684931519 15.992511415525115 -3.933150684931519 15.992511415525115 -5.933150684931519 12.992511415525115 -10.933150684931519 11.992511415525115 -12.933150684931519 7.992511415525115 -14.933150684931519 6.992511415525115 -15.933150684931519 4.992511415525115 -15.933150684931519 2.992511415525115 -16.93315068493152 -1.0074885844748849 -16.93315068493152 -3.007488584474885 -16.93315068493152 -5.007488584474885 -15.933150684931519 -7.007488584474885 -15.933150684931519 -10.007488584474885 -13.933150684931519 -12.007488584474885 -12.933150684931519 -15.007488584474885 -7.933150684931519 -16.007488584474885 -5.933150684931519 -16.007488584474885 -3.933150684931519 -17.007488584474885 -1.933150684931519 -17.007488584474885 2.066849315068481 -17.007488584474885 4.066849315068481 -15.007488584474885 7.066849315068481 -15.007488584474885 9.066849315068481 -10.007488584474885 13.066849315068481 -9.007488584474885 15.066849315068481 -5.007488584474885 16.06684931506848 -4.007488584474885 17.06684931506848 1.9925114155251151 17.06684931506848</Spot>
            <Spot ID="336318" name="ID336318" STD_INTENSITY_CH1="22.26675252697455" SOLIDITY="0.9822389666307859" QUALITY="910.0" POSITION_T="0.0" TOTAL_INTENSITY_CH1="230775.0" CONTRAST_CH1="0.9948595339882516" ELLIPSE_MINOR="17.02619535091659" ELLIPSE_THETA="1.3057152350530554" ELLIPSE_Y0="0.06124908722334814" FRAME="0" CIRCULARITY="0.9363990531486031" AREA="912.5000000000002" ELLIPSE_MAJOR="17.217891228068787" MEAN_INTENSITY_CH1="253.04276315789474" MAX_INTENSITY_CH1="255.0" MIN_INTENSITY_CH1="0.0" SNR_CH1="11.334868344974025" ELLIPSE_X0="0.002593896438507841" SHAPE_INDEX="3.663316558971327" MEDIAN_INTENSITY_CH1="255.0" VISIBILITY="1" RADIUS="17.04282168957679" POSITION_X="316.50748858447486" POSITION_Y="306.4331506849315" ELLIPSE_ASPECTRATIO="1.0112588792270538" POSITION_Z="0.0" PERIMETER="110.66005599470205" ROI_N_POINTS="36">3.9925114155251435 17.06684931506851 10.992511415525144 13.06684931506851 12.992511415525144 12.06684931506851 12.992511415525144 10.06684931506851 14.992511415525144 9.06684931506851 15.992511415525144 5.066849315068509 16.992511415525144 4.066849315068509 16.992511415525144 0.06684931506850944 16.992511415525144 -1.9331506849314906 15.992511415525144 -3.9331506849314906 15.992511415525144 -5.933150684931491 12.992511415525144 -10.93315068493149 11.992511415525144 -12.93315068493149 7.9925114155251435 -14.93315068493149 6.9925114155251435 -15.93315068493149 4.9925114155251435 -15.93315068493149 2.9925114155251435 -16.93315068493149 -1.0074885844748565 -16.93315068493149 -3.0074885844748565 -16.93315068493149 -5.0074885844748565 -15.93315068493149 -7.0074885844748565 -15.93315068493149 -10.007488584474856 -13.93315068493149 -12.007488584474856 -12.93315068493149 -15.007488584474856 -7.933150684931491 -16.007488584474856 -5.933150684931491 -16.007488584474856 -3.9331506849314906 -17.007488584474856 -1.9331506849314906 -17.007488584474856 2.0668493150685094 -17.007488584474856 4.066849315068509 -15.007488584474856 7.066849315068509 -15.007488584474856 9.06684931506851 -10.007488584474856 13.06684931506851 -9.007488584474856 15.06684931506851 -5.0074885844748565 16.06684931506851 -4.0074885844748565 17.06684931506851 1.9925114155251435 17.06684931506851</Spot>
        </SpotsInFrame>
        <SpotsInFrame frame="1">
            <Spot ID="336317" name="ID336317" STD_INTENSITY_CH1="22.26675252697455" SOLIDITY="0.9822389666307859" QUALITY="910.0" POSITION_T="1.0" TOTAL_INTENSITY_CH1="230775.0" CONTRAST_CH1="0.9948595339882516" ELLIPSE_MINOR="17.02619535091659" ELLIPSE_THETA="1.3057152350530554" ELLIPSE_Y0="0.06124908722334814" FRAME="1" CIRCULARITY="0.9363990531486031" AREA="912.5000000000002" ELLIPSE_MAJOR="17.217891228068787" MEAN_INTENSITY_CH1="253.04276315789474" MAX_INTENSITY_CH1="255.0" MIN_INTENSITY_CH1="0.0" SNR_CH1="11.334868344974025" ELLIPSE_X0="0.002593896438507841" SHAPE_INDEX="3.663316558971327" MEDIAN_INTENSITY_CH1="255.0" VISIBILITY="1" RADIUS="17.04282168957679" POSITION_X="321.50748858447486" POSITION_Y="302.4331506849315" ELLIPSE_ASPECTRATIO="1.0112588792270538" POSITION_Z="0.0" PERIMETER="110.66005599470205" ROI_N_POINTS="36">3.9925114155251435 17.06684931506851 10.992511415525144 13.06684931506851 12.992511415525144 12.06684931506851 12.992511415525144 10.06684931506851 14.992511415525144 9.06684931506851 15.992511415525144 5.066849315068509 16.992511415525144 4.066849315068509 16.992511415525144 0.06684931506850944 16.992511415525144 -1.9331506849314906 15.992511415525144 -3.9331506849314906 15.992511415525144 -5.933150684931491 12.992511415525144 -10.93315068493149 11.992511415525144 -12.93315068493149 7.9925114155251435 -14.93315068493149 6.9925114155251435 -15.93315068493149 4.9925114155251435 -15.93315068493149 2.9925114155251435 -16.93315068493149 -1.0074885844748565 -16.93315068493149 -3.0074885844748565 -16.93315068493149 -5.0074885844748565 -15.93315068493149 -7.0074885844748565 -15.93315068493149 -10.007488584474856 -13.93315068493149 -12.007488584474856 -12.93315068493149 -15.007488584474856 -7.933150684931491 -16.007488584474856 -5.933150684931491 -16.007488584474856 -3.9331506849314906 -17.007488584474856 -1.9331506849314906 -17.007488584474856 2.0668493150685094 -17.007488584474856 4.066849315068509 -15.007488584474856 7.066849315068509 -15.007488584474856 9.06684931506851 -10.007488584474856 13.06684931506851 -9.007488584474856 15.06684931506851 -5.0074885844748565 16.06684931506851 -4.0074885844748565 17.06684931506851 1.9925114155251435 17.06684931506851</Spot>
            <Spot ID="336315" name="ID336315" STD_INTENSITY_CH1="22.26675252697455" SOLIDITY="0.9822389666307861" QUALITY="910.0" POSITION_T="1.0" TOTAL_INTENSITY_CH1="230775.0" CONTRAST_CH1="0.9948595339882516" ELLIPSE_MINOR="17.026195350916595" ELLIPSE_THETA="1.3057152350530556" ELLIPSE_Y0="0.06124908722332005" FRAME="1" CIRCULARITY="0.936399053148603" AREA="912.5000000000001" ELLIPSE_MAJOR="17.21789122806879" MEAN_INTENSITY_CH1="253.04276315789474" MAX_INTENSITY_CH1="255.0" MIN_INTENSITY_CH1="0.0" SNR_CH1="11.334868344974025" ELLIPSE_X0="0.002593896438477291" SHAPE_INDEX="3.6633165589713275" MEDIAN_INTENSITY_CH1="255.0" VISIBILITY="1" RADIUS="17.042821689576787" POSITION_X="158.50748858447488" POSITION_Y="144.43315068493152" ELLIPSE_ASPECTRATIO="1.0112588792270538" POSITION_Z="0.0" PERIMETER="110.66005599470205" ROI_N_POINTS="36">3.992511415525115 17.06684931506848 10.992511415525115 13.066849315068481 12.992511415525115 12.066849315068481 12.992511415525115 10.066849315068481 14.992511415525115 9.066849315068481 15.992511415525115 5.066849315068481 16.992511415525115 4.066849315068481 16.992511415525115 0.06684931506848102 16.992511415525115 -1.933150684931519 15.992511415525115 -3.933150684931519 15.992511415525115 -5.933150684931519 12.992511415525115 -10.933150684931519 11.992511415525115 -12.933150684931519 7.992511415525115 -14.933150684931519 6.992511415525115 -15.933150684931519 4.992511415525115 -15.933150684931519 2.992511415525115 -16.93315068493152 -1.0074885844748849 -16.93315068493152 -3.007488584474885 -16.93315068493152 -5.007488584474885 -15.933150684931519 -7.007488584474885 -15.933150684931519 -10.007488584474885 -13.933150684931519 -12.007488584474885 -12.933150684931519 -15.007488584474885 -7.933150684931519 -16.007488584474885 -5.933150684931519 -16.007488584474885 -3.933150684931519 -17.007488584474885 -1.933150684931519 -17.007488584474885 2.066849315068481 -17.007488584474885 4.066849315068481 -15.007488584474885 7.066849315068481 -15.007488584474885 9.066849315068481 -10.007488584474885 13.066849315068481 -9.007488584474885 15.066849315068481 -5.007488584474885 16.06684931506848 -4.007488584474885 17.06684931506848 1.9925114155251151 17.06684931506848</Spot>
        </SpotsInFrame>
        </AllSpots>
        <AllTracks>
        <Track name="Track_0" TRACK_ID="0" TRACK_INDEX="0" NUMBER_SPOTS="2" NUMBER_GAPS="0" NUMBER_SPLITS="0" NUMBER_MERGES="0" NUMBER_COMPLEX="0" LONGEST_GAP="0" TRACK_DURATION="1.0" TRACK_START="0.0" TRACK_STOP="1.0" TRACK_DISPLACEMENT="3.1622776601683795" TRACK_X_LOCATION="158.00748858447488" TRACK_Y_LOCATION="142.93315068493152" TRACK_Z_LOCATION="0.0" TRACK_MEAN_SPEED="3.1622776601683795" TRACK_MAX_SPEED="3.1622776601683795" TRACK_MIN_SPEED="3.1622776601683795" TRACK_MEDIAN_SPEED="3.1622776601683795" TRACK_STD_SPEED="NaN" TRACK_MEAN_QUALITY="910.0" TOTAL_DISTANCE_TRAVELED="3.1622776601683795" MAX_DISTANCE_TRAVELED="3.1622776601683795" CONFINEMENT_RATIO="1.0" MEAN_STRAIGHT_LINE_SPEED="3.1622776601683795" LINEARITY_OF_FORWARD_PROGRESSION="1.0" MEAN_DIRECTIONAL_CHANGE_RATE="NaN">
            <Edge SPOT_SOURCE_ID="336316" SPOT_TARGET_ID="336315" LINK_COST="10.0" DIRECTIONAL_CHANGE_RATE="NaN" SPEED="3.1622776601683795" DISPLACEMENT="3.1622776601683795" EDGE_TIME="0.5" EDGE_X_LOCATION="158.00748858447488" EDGE_Y_LOCATION="142.93315068493152" EDGE_Z_LOCATION="0.0" />
        </Track>
        <Track name="Track_1" TRACK_ID="1" TRACK_INDEX="1" NUMBER_SPOTS="2" NUMBER_GAPS="0" NUMBER_SPLITS="0" NUMBER_MERGES="0" NUMBER_COMPLEX="0" LONGEST_GAP="0" TRACK_DURATION="1.0" TRACK_START="0.0" TRACK_STOP="1.0" TRACK_DISPLACEMENT="6.4031242374328485" TRACK_X_LOCATION="319.00748858447486" TRACK_Y_LOCATION="304.4331506849315" TRACK_Z_LOCATION="0.0" TRACK_MEAN_SPEED="6.4031242374328485" TRACK_MAX_SPEED="6.4031242374328485" TRACK_MIN_SPEED="6.4031242374328485" TRACK_MEDIAN_SPEED="6.4031242374328485" TRACK_STD_SPEED="NaN" TRACK_MEAN_QUALITY="910.0" TOTAL_DISTANCE_TRAVELED="6.4031242374328485" MAX_DISTANCE_TRAVELED="6.4031242374328485" CONFINEMENT_RATIO="1.0" MEAN_STRAIGHT_LINE_SPEED="6.4031242374328485" LINEARITY_OF_FORWARD_PROGRESSION="1.0" MEAN_DIRECTIONAL_CHANGE_RATE="NaN">
            <Edge SPOT_SOURCE_ID="336318" SPOT_TARGET_ID="336317" LINK_COST="41.0" DIRECTIONAL_CHANGE_RATE="NaN" SPEED="6.4031242374328485" DISPLACEMENT="6.4031242374328485" EDGE_TIME="0.5" EDGE_X_LOCATION="319.00748858447486" EDGE_Y_LOCATION="304.4331506849315" EDGE_Z_LOCATION="0.0" />
        </Track>
        </AllTracks>
        <FilteredTracks>
        <TrackID TRACK_ID="0" />
        <TrackID TRACK_ID="1" />
        </FilteredTracks>
    </Model>
    <Settings>
        <ImageData filename="Untitled" folder="" width="512" height="512" nslices="1" nframes="2" pixelwidth="1.0" pixelheight="1.0" voxeldepth="1.0" timeinterval="1.0" />
        <BasicSettings xstart="0" xend="511" ystart="0" yend="511" zstart="0" zend="0" tstart="0" tend="1" />
        <DetectorSettings DETECTOR_NAME="THRESHOLD_DETECTOR" TARGET_CHANNEL="1" INTENSITY_THRESHOLD="254.0" SIMPLIFY_CONTOURS="true" />
        <InitialSpotFilter feature="QUALITY" value="0.22185452133476247" isabove="true" />
        <SpotFilterCollection />
        <TrackerSettings TRACKER_NAME="SIMPLE_SPARSE_LAP_TRACKER" CUTOFF_PERCENTILE="0.9" ALTERNATIVE_LINKING_COST_FACTOR="1.05" BLOCKING_VALUE="Infinity">
        <Linking LINKING_MAX_DISTANCE="15.0">
            <FeaturePenalties />
        </Linking>
        <GapClosing ALLOW_GAP_CLOSING="true" GAP_CLOSING_MAX_DISTANCE="15.0" MAX_FRAME_GAP="2">
            <FeaturePenalties />
        </GapClosing>
        <TrackSplitting ALLOW_TRACK_SPLITTING="false" SPLITTING_MAX_DISTANCE="15.0">
            <FeaturePenalties />
        </TrackSplitting>
        <TrackMerging ALLOW_TRACK_MERGING="false" MERGING_MAX_DISTANCE="15.0">
            <FeaturePenalties />
        </TrackMerging>
        </TrackerSettings>
        <TrackFilterCollection />
        <AnalyzerCollection>
        <SpotAnalyzers>
            <Analyzer key="Manual spot color" />
            <Analyzer key="Spot intensity" />
            <Analyzer key="EXTRACK_PROBABILITIES" />
            <Analyzer key="Spot contrast and SNR" />
            <Analyzer key="Spot fit 2D ellipse" />
            <Analyzer key="Spot 2D shape descriptors" />
        </SpotAnalyzers>
        <EdgeAnalyzers>
            <Analyzer key="Directional change" />
            <Analyzer key="Edge speed" />
            <Analyzer key="Edge target" />
            <Analyzer key="Edge location" />
            <Analyzer key="Manual edge color" />
        </EdgeAnalyzers>
        <TrackAnalyzers>
            <Analyzer key="Branching analyzer" />
            <Analyzer key="Track duration" />
            <Analyzer key="Track index" />
            <Analyzer key="Track location" />
            <Analyzer key="Track speed" />
            <Analyzer key="Track quality" />
            <Analyzer key="Track motility analysis" />
        </TrackAnalyzers>
        </AnalyzerCollection>
    </Settings>
    <GUIState state="ConfigureViews" />
    <DisplaySettings>{
    "name": "CurrentDisplaySettings",
    "spotUniformColor": "204, 51, 204, 255",
    "spotColorByType": "DEFAULT",
    "spotColorByFeature": "UNIFORM_COLOR",
    "spotDisplayRadius": 1.0,
    "spotDisplayedAsRoi": true,
    "spotMin": 0.0,
    "spotMax": 10.0,
    "spotShowName": false,
    "trackMin": 0.0,
    "trackMax": 10.0,
    "trackColorByType": "TRACKS",
    "trackColorByFeature": "TRACK_INDEX",
    "trackUniformColor": "204, 204, 51, 255",
    "undefinedValueColor": "0, 0, 0, 255",
    "missingValueColor": "89, 89, 89, 255",
    "highlightColor": "51, 230, 51, 255",
    "trackDisplayMode": "FULL",
    "colormap": "Jet",
    "limitZDrawingDepth": false,
    "drawingZDepth": 10.0,
    "fadeTracks": true,
    "fadeTrackRange": 30,
    "useAntialiasing": true,
    "spotVisible": true,
    "trackVisible": true,
    "font": {
        "name": "Arial",
        "style": 1,
        "size": 12,
        "pointSize": 12.0,
        "fontSerializedDataVersion": 1
    },
    "lineThickness": 1.0,
    "selectionLineThickness": 4.0,
    "trackschemeBackgroundColor1": "128, 128, 128, 255",
    "trackschemeBackgroundColor2": "192, 192, 192, 255",
    "trackschemeForegroundColor": "0, 0, 0, 255",
    "trackschemeDecorationColor": "0, 0, 0, 255",
    "trackschemeFillBox": false,
    "spotFilled": false,
    "spotTransparencyAlpha": 1.0
    }</DisplaySettings>
    </TrackMate>
    '''

    # write file
    with open(path, "w") as f:
        f.write(xml)

    return path