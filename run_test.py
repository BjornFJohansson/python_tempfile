#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile, os

pydna_data_dir    = tempfile.mkdtemp(prefix="pydna_data_dir_")
pydna_log_dir     = tempfile.mkdtemp(prefix="pydna_log_dir_")
pydna_config_dir  = tempfile.mkdtemp(prefix="pydna_config_dir_")


print(pydna_data_dir)
print(pydna_log_dir)
print(pydna_config_dir)


os.makedirs(pydna_data_dir)
os.makedirs(pydna_log_dir)
os.makedirs(pydna_config_dir)

