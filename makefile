serv:
	git rm -rf water_heating_system/
	cp -R ../Stydu/Work/water_heating_system .
	git add water_heating_system/
	git commit -m "water_debug"
	git push origin main