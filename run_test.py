#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile, os

pydna_data_dir    = tempfile.mkdtemp(prefix="pydna_data_dir_")
pydna_log_dir     = tempfile.mkdtemp(prefix="pydna_log_dir_")
pydna_config_dir  = tempfile.mkdtemp(prefix="pydna_config_dir_")


print(pydna_data_dir)
print(pydna_log_dir)
print(pydna_config_dir)



print( os.path.exists(pydna_data_dir)    )
print( os.path.exists(pydna_log_dir)     )
print( os.path.exists(pydna_config_dir)  )

