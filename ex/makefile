python = python3
autogame = "auto_game.py"
dump2txt = "/mnt/e/projects/research/football/env/gfootball/dump_to_txt.py"

dump_dir = /mnt/e/projects/research/football/dumps
dump_filename = shutdown_20200105-154643745915.dump
dump_path = $(dump_dir)/$(dump_filename)
txt_filename = out.txt
txt_path = $(dump_dir)/$(txt_filename)

autogame_args = --action_set=full --players='' --noreal_time --dump_dir=$(dump_dir)

autogame:
	$(python) $(autogame) $(autogame_args)

dump2txt:
	$(python) $(dump2txt) --trace_file=$(dump_path) --output=$(txt_path)