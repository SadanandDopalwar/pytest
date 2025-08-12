def test_write_file(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("hello pytest")
    assert file.read_text() == "hello pytest"
#Temporary files & folders that automatically clean up.