%define         qtmame		qtmame
%define		qtmame_ver	2.0.2
Summary:	Unix/X11 port of M.A.M.E. - arcade machine emulator
Summary(es):	X-Mame Arcade Game Emulator
Summary(ko):	X윈도우 시스템을 위한 업소용 게임기 에물레이터
Summary(pl):	Port emulatora M.A.M.E. dzia쿪j켧y w 턳odowisku Unix/X11
Summary(pt_BR):	Emulador de Arcades X-Mame
Name:		xmame
Version:	0.67.2
Release:	2
License:	GPL
Group:		Applications/Emulators
#Source0Download:	http://x.mame.net/xmame-doc-7.html
Source0:	http://x.mame.net/download/%{name}-%{version}.tar.bz2
Source1:	http://lecha.homelinux.com/ingenio/archivos/%{qtmame}-%{qtmame_ver}.tar.gz
Source2:	%{name}-SDL.desktop
Source3:	%{name}-x11.desktop
Source4:	%{name}-alsa_0.5.c
Source5:	%{name}-alsa_0.9.c
Source6:        %{name}.png
Source7:        xmame-qtmame.desktop
Source8:        xmame-qtmame_pl.ts
Patch0:		%{name}-alsa.patch
Patch1:         %{qtmame}-pl.patch
URL:		http://x.mame.net/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	alsa-driver-devel >= 0.9
BuildRequires:	libusb
%ifarch %{ix86} alpha
BuildRequires:	svgalib-devel
%endif
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-Mame the UNIX/X11 port of Mame project. It makes Mame arcade
emulator available on *ix machines using the X11R6 X-Window system
(and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if you
have original ROM images of a supported arcade game, you can play the
game.

%description -l pl
X-Mame to uniksowy/X-owy port projektu Mame. Pozwala uruchamia�
emulator Mame na maszynach uniksowych z X11R6 Window System (a tak풽
linuksowych z SVGAlibem).

Mame to emulator maszyny wirtualnej: zawiera emulatory Z80, 6502,
68000 i ostatnie I86, po낢czone z r璨nymi emulatorami sprz�tu do gier.
Ka풼y emulator zawiera pe쿻y opis sprz�tu, mapy pami�ci, obrazu,
d펧i�ku itp., co pozwala gra� w gry pod warunkiem posiadania
oryginalnych obraz�w ROM.

%description -l pt_BR
X-Mame � o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator dispon�vel em m�quinas *ix usando o sistema X-Window
X11R6 (e sobre Linux usando SVGAlib tamb�m). Mame � uma emulador de
m�quinas virtuais: ele inclui um Z80, 6502, 68000 e recentemente
microprocessadores I86, agregando uma grande quantidade de m�quinas de
arcade. Cada emulador cont�m uma descri豫o sobre o hardware, mapas de
mem�ria, v�deo, som, etc, tornando poss�vel que voc� possa jogar suas
ROMS originais.

%package common
Summary:	Xmame - common files
Summary(pl):	Xmame - wsp�lne pliki
Group:		Applications/Emulators

%description common
X-Mame the UNIX/X11 port of Mame project. It makes Mame arcade
emulator available on *ix machines using the X11R6 X-Window system
(and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if you
have original ROM images of a supported arcade game, you can play the
game.

This package contains base, common xmame files, required to run all
versions of xmame.

%description common -l pl
X-Mame to uniksowy/X-owy port projektu Mame. Pozwala uruchamia�
emulator Mame na maszynach uniksowych z X11R6 Window System (a tak풽
linuksowych z SVGAlibem).

Mame to emulator maszyny wirtualnej: zawiera emulatory Z80, 6502,
68000 i ostatnie I86, po낢czone z r璨nymi emulatorami sprz�tu do gier.
Ka풼y emulator zawiera pe쿻y opis sprz�tu, mapy pami�ci, obrazu,
d펧i�ku itp., co pozwala gra� w gry pod warunkiem posiadania
oryginalnych obraz�w ROM.

Ten pakiet zawiera podstawowe, wsp�lne pliki X-Mame, potrzebne do
uruchamiania ka풼ej wersji emulatora.

%package SDL
Summary:	Xmame with SDL graphic output
Summary(es):	X-Mame Arcade Game Emulator - SDL
Summary(pl):	Xmame z wyj턢iem graficznym SDL
Summary(pt_BR):	Emulador de Arcades X-Mame - SDL
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description SDL
This package has xmame binaries compiled for SDL graphics output.

%description SDL -l pl
Ten pakiet zawiera binaria X-Mame z wyj턢iem grafiki przez SDL.

%description SDL -l pt_BR
X-Mame � o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator dispon�vel em m�quinas *ix usando o sistema X-Window
X11R6 (e sobre Linux usando SVGAlib tamb�m).

%package svgalib
Summary:	xmame - svgalib version
Summary(es):	X-Mame Arcade Game Emulator - svgalib
Summary(pl):	xmame - wersja z wyj턢iem svgalib
Summary(pt_BR):	Emulador de Arcades X-Mame - svgalib
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description svgalib
This package has xmame binaries compiled for svgalib graphic output.

%description svgalib -l pl
Ten pakiet zawiera binaria X-Mame z wyj턢iem grafiki przez SVGAlib.

%description svgalib -l pt_BR
X-Mame � o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator dispon�vel em m�quinas *ix usando o sistema X11 (e
sobre Linux usando SVGAlib tamb�m).

%package x11
Summary:	xmame - x11 version
Summary(es):	X-Mame Arcade Game Emulator - X11
Summary(pl):	xmame - wersja z wyj턢iem x11
Summary(pt_BR):	Emulador de Arcades X-Mame - X11
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description x11
This package has xmame binaries compiled for x11 graphic output.

%description x11 -l pl
Ten pakiet zawiera binaria X-Mame z wyj턢iem grafiki pod X11.

%description x11 -l pt_BR
X-Mame � o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator dispon�vel em m�quinas *ix usando o sistema X-Window
X11R6 (e sobre Linux usando SVGAlib tamb�m).

%package screensaver
Summary:	xmame - screensaver
Summary(pl):	xmame - wygaszacz ekranu
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description screensaver
The xmame screensaver.

%description screensaver -l pl
Wygaszacz ekranu X-Mame.

%package qtmame
Summary:	Qtmame - graphic interface for xmame
Summary(pl):	Qtmame - graficzny interfejs dla xmame
Group:		Applications/Emulator
URL:		http://move.to/ingenio
Requires:	%{name}-common = %{version}
Provides:	qtmame
Obsoletes:	qtmame

%description qtmame
Graphic interface for xmame.

%description qtmame -l pl
Graficzny interfejs dla xmame.

%prep
%setup -q -a1
#%patch0 -p1
%patch1 -p1
install %{SOURCE4} src/unix/sysdep/dsp-drivers/alsa_0.5.c
install %{SOURCE5} src/unix/sysdep/dsp-drivers/alsa_0.9.c
install %{SOURCE8} %{qtmame}-%{qtmame_ver}/qtmame/qtmame_pl.ts
lrelease %{qtmame}-%{qtmame_ver}/qtmame/qtmame.pro

%build
cd %{qtmame}-%{qtmame_ver}
%configure2_13

%{__make}

cd ..
%{__make} -f makefile.unix \
	PREFIX=%{_prefix} \
	XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name} \
	CC="%{__cc}" CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
	LD="%{__cc} %{rpmldflags}" \
	DISPLAY_METHOD=SDL \
	SOUND_ESOUND=1 \
	SOUND_ALSA=1 \
	SOUND_ARTS_TEIRA=1 \
	SOUND_ARTS_SMOTEK=1 \
	SOUND_SDL=1

%ifarch %{ix86} alpha
%{__make} -f makefile.unix \
	PREFIX=%{_prefix} \
	XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name} \
	CC="%{__cc}" CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
	LD="%{__cc} %{rpmldflags}" \
	DISPLAY_METHOD=svgalib \
	SOUND_ESOUND=1 \
	SOUND_ALSA=1 \
	SOUND_ARTS_TEIRA=1 \
	SOUND_ARTS_SMOTEK=1 \
	SOUND_SDL=1
%endif

%{__make} -f makefile.unix \
	PREFIX=%{_prefix} \
	XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name} \
	CC="%{__cc}" CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
	LD="%{__cc} %{rpmldflags}" \
	DISPLAY_METHOD=x11 \
	SOUND_ESOUND=1 \
	SOUND_ALSA=1 \
	SOUND_ARTS_TEIRA=1 \
	SOUND_ARTS_SMOTEK=1 \
	SOUND_SDL=1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6} \
	$RPM_BUILD_ROOT%{_datadir}/games/%{name}/{cab,rc} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games/Arcade} \
	$RPM_BUILD_ROOT%{_datadir}/qtmame
install xmame.SDL $RPM_BUILD_ROOT%{_bindir}
%ifarch %{ix86} alpha
install xmame.svgalib $RPM_BUILD_ROOT%{_bindir}
%endif
install xmame.x11 $RPM_BUILD_ROOT%{_bindir}
install contrib/tools/xmame-screensaver $RPM_BUILD_ROOT%{_bindir}
cp -R src/unix/cab/ $RPM_BUILD_ROOT%{_datadir}/games/%{name}

install src/unix/doc/xmame.6 $RPM_BUILD_ROOT%{_mandir}/man6
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
#install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE7} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

install %{qtmame}-%{qtmame_ver}/qtmame/qtmame $RPM_BUILD_ROOT%{_bindir}
install %{qtmame}-%{qtmame_ver}/qtmame/qtmame.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{qtmame}-%{qtmame_ver}/qtmame/bkground.png $RPM_BUILD_ROOT%{_datadir}/qtmame
install %{qtmame}-%{qtmame_ver}/qtmame/*.qm $RPM_BUILD_ROOT%{_datadir}/qtmame
install %{qtmame}-%{qtmame_ver}/qtmame/listado020 $RPM_BUILD_ROOT%{_datadir}/qtmame
install %{qtmame}-%{qtmame_ver}/qtmame/qtmame3.png $RPM_BUILD_ROOT%{_datadir}/qtmame

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc doc/*
%{_mandir}/man6/*
%{_datadir}/games/%{name}
%{_pixmapsdir}/xmame.png

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}.SDL
#%{_applnkdir}/Games/Arcade/%{name}-SDL.desktop

%ifarch %{ix86} alpha
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}.svgalib
%endif

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}.x11
#%{_applnkdir}/Games/Arcade/%{name}-x11.desktop

%files screensaver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmame-screensaver

%files qtmame
%defattr(644,root,root,755)
%doc %{qtmame}-%{qtmame_ver}/{AUTHORS,README,README-us,TODO,qtmame/docs/en/*.html}
%attr(755,root,root) %{_bindir}/qtmame
%{_datadir}/qtmame
%{_pixmapsdir}/*
%{_applnkdir}/Games/Arcade/%{name}-qtmame.desktop
