CC=clang
LIBPATH=../gym/envs/space_fortress/shared
USE_GUI=yes
CREATE_BINARY=no
GUI=-D GUI_INTERFACE
ifneq ($(USE_GUI),gcc)
	GUI:=
endif	

define build
	$(CC) -march=native `pkg-config --cflags cairo` -Wall -g -fPIC -c $(1)/myvars.c $(1)/DE_Minimal.c $(1)/HM.c $(1)/TCOL.c $(1)/RS.c -Wno-dangling-else -Wno-switch -O3 $(GUI);
	$(CC) -march=native `pkg-config --cflags cairo --libs cairo` -shared -o $(2)_frame_lib.so myvars.o HM.o RS.o TCOL.o DE_Minimal.o -O3 $(GUI);
	#$(CC) -march=native `pkg-config --cflags cairo pkg-config --libs cairo pkg-config --cflags gtk+-3.0 pkg-config --libs gtk+-3.0 ` -Wall -g -fPIC $(1)/myvars.c $(1)/TCOL.c $(1)/DE_Minimal.c $(1)/HM.c $(1)/RS.c  -lm -o Control -Wno-dangling-else -Wno-switch $(GUI);
	
	@mv *.o $(1)
	@mv *.so $(LIBPATH)
	@echo "Shared library $(2)_frame_lib.so sucessfully made and installed"
endef

AIM:
	$(call build, AIM_Cairo, aim)
SF:
	$(call build, SF_Cairo, sf)
SFC:
	$(call build, SFC_Cairo, control)

all: AIM SF SFC

clean:
	@rm AIM_Cairo/*.o SF_Cairo/*.o SFC_Cairo/*.o $(LIBPATH)/*.so