<?php
require_once 'lib/function.php';

require_once 'lib/conf.php';

create_db();
create_index_ids();
create_index_source();

load_file();
