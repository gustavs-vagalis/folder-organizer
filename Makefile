all:
	@echo Run \'make install\' to install to /bin.

install:
	@cp ./main.py /bin/organize
	@chmod 775 /bin/organize

uninstall:
	@rm /bin/organize