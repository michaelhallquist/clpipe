import pytest

from clpipe.bids_conversion import convert2bids

@pytest.mark.skip(reason="Erroneously causing submission.")
def test_dcm2bids(clpipe_dicom_dir, config_file):
    convert2bids(
        dcm2bids = True,
        config_file = config_file,
        dicom_dir = clpipe_dicom_dir / "sub",
        dicom_dir_format = "{subject}"
    )

    assert True

@pytest.mark.skip(reason="Erroneously causing submission.")
def test_dcm2bids_sub_session(clpipe_dicom_dir, config_file):
    convert2bids(
        dcm2bids = True,
        config_file = config_file,
        dicom_dir = clpipe_dicom_dir / "sub_session",
        dicom_dir_format = "{subject}/{session}"
    )

    assert True

@pytest.mark.skip(reason="Erroneously causing submission.")
def test_dcm2bids_sub_session_flat(clpipe_dicom_dir, config_file):
    convert2bids(
        dcm2bids = True,
        config_file = config_file,
        dicom_dir = clpipe_dicom_dir / "sub_session_flat",
        dicom_dir_format = "{subject}_{session}"
    )

    assert True

@pytest.mark.skip(reason="Erroneously causing submission.")
def test_dcm2bids_session_sub(clpipe_dicom_dir, config_file):
    convert2bids(
        dcm2bids = True,
        config_file = config_file,
        dicom_dir = clpipe_dicom_dir / "session_sub",
        dicom_dir_format = "{session}/{subject}"
    )

    assert True

@pytest.mark.skip(reason="Erroneously causing submission.")
def test_dcm2bids_session_sub_flat(clpipe_dicom_dir, config_file):
    convert2bids(
        dcm2bids = True,
        config_file = config_file,
        dicom_dir = clpipe_dicom_dir / "session_sub_flat",
        dicom_dir_format = "{session}_{subject}"
    )

    assert True

@pytest.mark.skip(reason="Erroneously causing submission.")
def test_heudiconv(clpipe_dicom_dir, config_file):
    convert2bids(
        dcm2bids = False,
        config_file = config_file,
        dicom_dir = clpipe_dicom_dir / "sub",
        dicom_dir_format = "{subject}"
    )

    assert True