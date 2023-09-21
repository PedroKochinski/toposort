PYTHON = python3
PROGRAM = toposort

all: $(PROGRAM)

$(PROGRAM): toposort.py
	@echo '#!/usr/bin/env $(PYTHON)' > $(PROGRAM)
	@cat toposort.py >> $(PROGRAM)
	@chmod +x $(PROGRAM)
	@echo Executável $(PROGRAM) criado

clean:
	-rm -f $(PROGRAM) *~
 
purge: clean
	-rm -f $(PROGRAM)