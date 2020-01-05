python = python3
football_base = /mnt/e/projects/research/football/env/gfootball
ex_base = /mnt/e/projects/research/football/ex
dump_filename = shutdown_20200105-154643745915.dump
txt_filename = out.txt
dump_dir = /mnt/e/projects/research/football/dumps

dump_path = $(dump_dir)/$(dump_filename)
txt_path = $(dump_dir)/$(txt_filename)

autogame = $(ex_base)/auto_game.py
dump2txt = $(football_base)/dump_to_txt.py

autogame_args = --action_set=full --players='' --noreal_time --dump_dir=$(dump_dir)
autogame:
	$(python) $(autogame) $(autogame_args)

dump2txt_args = --trace_file=$(dump_path) --output=$(txt_path)
dump2txt:
	$(python) $(dump2txt) $(dump2txt_args)