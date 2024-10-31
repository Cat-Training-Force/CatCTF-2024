all:
	bash ./build.sh && bash ./run.sh

build:
	bash ./build.sh

stop:
	bash ./stop.sh

clean:
	bash stop.sh ; bash ./delete.sh

rebuild:
	bash stop.sh ; bash ./delete.sh ; bash ./build.sh ; bash ./run.sh

push:
	bash ./push.sh

publish:
	bash ./build.sh && bash ./push.sh