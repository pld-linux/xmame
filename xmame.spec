#
# Conditional build:
%bcond_without	svga	# don't build svga version
%bcond_without	qt	# don't build qtmame
#
%ifnarch %{ix86} alpha ppc
%undefine      	with_svga
%endif
%define         qtmame		qtmame
%define		qtmame_ver	2.0.4
Summary:	Unix/X11 port of M.A.M.E. - arcade machine emulator
Summary(es):	X-Mame Arcade Game Emulator
Summary(ko):	X윈도우 시스템을 위한 업소용 게임기 에물레이터
Summary(pl):	Port emulatora M.A.M.E. dzia쿪j켧y w 턳odowisku Unix/X11
Summary(pt_BR):	Emulador de Arcades X-Mame
Name:		xmame
Version:	0.80.1
Release:	1
License:	GPL
Group:		Applications/Emulators
#Source0Download:	http://x.mame.net/xmame-doc-7.html
Source0:	http://x.mame.net/download/%{name}-%{version}.tar.bz2
# Source0-md5:	f2e51b0a695ee508ea76df86dd426730
Source1:	http://lecha.homelinux.com/ingenio/archivos/%{qtmame}-%{qtmame_ver}.tar.gz
# Source1-md5:	28fcd7859d0ad4f42091923cb2932ba2
Source2:	%{name}-SDL.desktop
Source3:	%{name}-x11.desktop
Source4:	%{name}-alsa_0.5.c
Source5:	%{name}-alsa_0.9.c
Source6:	%{name}.png
Source7:	xmame-qtmame.desktop
Source8:	xmame-qtmame_pl.ts
Source9:	http://x.mame.net/download/%{name}-doc.pdf
# Source9-md5:	650c7907d5b51d5e713593bf00b2db39
Patch0:		%{name}-alsa.patch
Patch1:		%{qtmame}-pl.patch
Patch2:		%{qtmame}-version.patch
URL:		http://x.mame.net/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	alsa-driver-devel >= 0.9
BuildRequires:	artsc-devel
BuildRequires:	libusb-devel
%{?with_svga:BuildRequires:	svgalib-devel}
%{?with_qt:BuildRequires:	qt-devel >= 3.0}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMame the UNIX/X11 port of Mame project. It makes Mame arcade
emulator available on *ix machines using the X11R6 X-Window system
(and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if you
have original ROM images of a supported arcade game, you can play the
game.

%description -l pl
XMame to uniksowy/X-owy port projektu Mame. Pozwala uruchamia�
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
Summary:	XMame - common files
Summary(pl):	XMame - wsp�lne pliki
Group:		Applications/Emulators

%description common
XMame the UNIX/X11 port of Mame project. It makes Mame arcade
emulator available on *ix machines using the X11R6 X-Window system
(and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if you
have original ROM images of a supported arcade game, you can play the
game.

This package contains base, common XMame files, required to run all
versions of XMame.

%description common -l pl
XMame to uniksowy/X-owy port projektu Mame. Pozwala uruchamia�
emulator Mame na maszynach uniksowych z X11R6 Window System (a tak풽
linuksowych z SVGAlibem).

Mame to emulator maszyny wirtualnej: zawiera emulatory Z80, 6502,
68000 i ostatnie I86, po낢czone z r璨nymi emulatorami sprz�tu do gier.
Ka풼y emulator zawiera pe쿻y opis sprz�tu, mapy pami�ci, obrazu,
d펧i�ku itp., co pozwala gra� w gry pod warunkiem posiadania
oryginalnych obraz�w ROM.

Ten pakiet zawiera podstawowe, wsp�lne pliki XMame, potrzebne do
uruchamiania ka풼ej wersji emulatora.

%package SDL
Summary:	XMame with SDL graphic output
Summary(es):	XMame Arcade Game Emulator - SDL
Summary(pl):	XMame z wyj턢iem graficznym SDL
Summary(pt_BR):	Emulador de Arcades XMame - SDL
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description SDL
This package has XMame binaries compiled for SDL graphics output.

%description SDL -l pl
Ten pakiet zawiera binaria XMame z wyj턢iem grafiki przez SDL.

%description SDL -l pt_BR
XMame � o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator dispon�vel em m�quinas *ix usando o sistema X-Window
X11R6 (e sobre Linux usando SVGAlib tamb�m).

%package svgalib
Summary:	XMame - svgalib version
Summary(es):	XMame Arcade Game Emulator - svgalib
Summary(pl):	XMame - wersja z wyj턢iem svgalib
Summary(pt_BR):	Emulador de Arcades XMame - svgalib
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description svgalib
This package has XMame binaries compiled for svgalib graphic output.

%description svgalib -l pl
Ten pakiet zawiera binaria XMame z wyj턢iem grafiki przez SVGAlib.

%description svgalib -l pt_BR
XMame � o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator dispon�vel em m�quinas *ix usando o sistema X11 (e
sobre Linux usando SVGAlib tamb�m).

%package x11
Summary:	XMame - x11 version
Summary(es):	XMame Arcade Game Emulator - X11
Summary(pl):	XMame - wersja z wyj턢iem x11
Summary(pt_BR):	Emulador de Arcades XMame - X11
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description x11
This package has XMame binaries compiled for x11 graphic output.

%description x11 -l pl
Ten pakiet zawiera binaria XMame z wyj턢iem grafiki pod X11.

%description x11 -l pt_BR
XMame � o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator dispon�vel em m�quinas *ix usando o sistema X-Window
X11R6 (e sobre Linux usando SVGAlib tamb�m).

%package screensaver
Summary:	XMame - screensaver
Summary(pl):	XMame - wygaszacz ekranu
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description screensaver
The XMame screensaver.

%description screensaver -l pl
Wygaszacz ekranu XMame.

%package qtmame
Summary:	Qtmame - graphic interface for XMame
Summary(pl):	Qtmame - graficzny interfejs dla XMame
Group:		Applications/Emulator
URL:		http://move.to/ingenio
Requires:	%{name}-common = %{version}
Provides:	qtmame
Obsoletes:	qtmame

%description qtmame
Graphic interface for XMame.

%description qtmame -l pl
Graficzny interfejs dla XMame.

%package xmess-x11
Summary:	xmess - a virtual machine emulator for x11
Summary(pl):	xmess - emulator maszyny wirtualnej dla x11
Group:		Applications/Emulator
Requires:	%{name}-common = %{version}

%description xmess-x11
Mess is just like mame - a virtual machine emulator, only it
doesn't emulate arcade machines but rather computers and consoles.
This package contains binaries for x11.

%description xmess-x11 -l pl
Mess to to samo co mame - emulator maszyny wirtualnej, tyle 풽
nie emuluje on automat�w arcade'owych a komputery i konsole.
Ten pakiet zawiera binaria dla x11.

%package xmess-SDL
Summary:	xmess - a virtual machine emulator for SDL
Summary(pl):	xmess - emulator maszyny wirtualnej dla SDL
Group:		Applications/Emulator
Requires:	%{name}-common = %{version}

%description xmess-SDL
Mess is just like mame - a virtual machine emulator, only it
doesn't emulate arcade machines but rather computers and consoles.
This package contains binaries for SDL.

%description xmess-SDL -l pl
Mess to to samo co mame - emulator maszyny wirtualnej, tyle 풽
nie emuluje on automat�w arcade'owych a komputery i konsole.
Ten pakiet zawiera binaria dla SDL.

%package xmess-svgalib
Summary:	xmess - a virtual machine emulator for svgalib
Summary(pl):	xmess - emulator maszyny wirtualnej dla svgalib
Group:		Applications/Emulator
Requires:	%{name}-common = %{version}

%description xmess-svgalib
Mess is just like mame - a virtual machine emulator, only it
doesn't emulate arcade machines but rather computers and consoles.
This package contains binaries for svgalib.

%description xmess-svgalib -l pl
Mess to to samo co mame - emulator maszyny wirtualnej, tyle 풽
nie emuluje on automat�w arcade'owych a komputery i konsole.
Ten pakiet zawiera binaria dla svgalib.

%prep
%setup -q -a1
#%patch0 -p1
%patch1 -p1
%patch2 -p1
install %{SOURCE4} src/unix/sysdep/dsp-drivers/alsa_0.5.c
install %{SOURCE5} src/unix/sysdep/dsp-drivers/alsa_0.9.c
install %{SOURCE9} doc/
%if %{with qt}
install %{SOURCE8} %{qtmame}-%{qtmame_ver}/qtmame/qtmame_pl.ts
lrelease %{qtmame}-%{qtmame_ver}/qtmame/qtmame.pro
%endif

%build
%if %{with qt}
cd %{qtmame}-%{qtmame_ver}
%configure2_13

%{__make}

cd ..
%endif

%{__make} -f makefile.unix \
	TARGET=mess \
        PREFIX=%{_prefix} \
        XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name} \
        CC="%{__cc}" CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
        LD="%{__cc} %{rpmldflags}" \
        DISPLAY_METHOD=SDL \
        SOUND_ESOUND=1 \
        SOUND_ALSA=1 \
        SOUND_ARTS_TEIRA=1 \
        SOUND_ARTS_SMOTEK=1 \
        SOUND_SDL=1 \
        XMAME_NET=1

%{__make} -f makefile.unix \
	TARGET=mess \
        PREFIX=%{_prefix} \
        XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name} \
        CC="%{__cc}" CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
        LD="%{__cc} %{rpmldflags}" \
        DISPLAY_METHOD=x11 \
        SOUND_ESOUND=1 \
        SOUND_ALSA=1 \
        SOUND_ARTS_TEIRA=1 \
        SOUND_ARTS_SMOTEK=1 \
        SOUND_SDL=1 \
        XMAME_NET=1

%if %{with svga}
%{__make} -f makefile.unix \
	TARGET=mess \
        PREFIX=%{_prefix} \
        XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name} \
        CC="%{__cc}" CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
        LD="%{__cc} %{rpmldflags}" \
        DISPLAY_METHOD=svgalib \
        SOUND_ESOUND=1 \
        SOUND_ALSA=1 \
        SOUND_ARTS_TEIRA=1 \
        SOUND_ARTS_SMOTEK=1 \
        SOUND_SDL=1 \
        XMAME_NET=1
%endif

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
	SOUND_SDL=1 \
	XMAME_NET=1

%if %{with svga}
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
	SOUND_SDL=1 \
	XMAME_NET=1
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
	SOUND_SDL=1 \
	XMAME_NET=1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6} \
	$RPM_BUILD_ROOT%{_datadir}/games/%{name}/{cab,rc} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games/Arcade} \
	$RPM_BUILD_ROOT%{_datadir}/qtmame
install xmame.SDL $RPM_BUILD_ROOT%{_bindir}

%if %{with svga}
install xmame.svgalib $RPM_BUILD_ROOT%{_bindir}
install xmess.svgalib $RPM_BUILD_ROOT%{_bindir}
%endif

install xmame.x11 $RPM_BUILD_ROOT%{_bindir}
install xmess.x11 $RPM_BUILD_ROOT%{_bindir}
install xmess.SDL $RPM_BUILD_ROOT%{_bindir}
install contrib/tools/xmame-screensaver $RPM_BUILD_ROOT%{_bindir}
cp -R src/unix/cab/ $RPM_BUILD_ROOT%{_datadir}/games/%{name}

install src/unix/doc/xmame.6 $RPM_BUILD_ROOT%{_mandir}/man6
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
#install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

%if %{with qt}
install %{SOURCE7} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

install %{qtmame}-%{qtmame_ver}/qtmame/qtmame $RPM_BUILD_ROOT%{_bindir}
install %{qtmame}-%{qtmame_ver}/qtmame/qtmame.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{qtmame}-%{qtmame_ver}/qtmame/bkground.png $RPM_BUILD_ROOT%{_datadir}/qtmame
install %{qtmame}-%{qtmame_ver}/qtmame/*.qm $RPM_BUILD_ROOT%{_datadir}/qtmame
install %{qtmame}-%{qtmame_ver}/qtmame/listado020 $RPM_BUILD_ROOT%{_datadir}/qtmame
install %{qtmame}-%{qtmame_ver}/qtmame/qtmame3.png $RPM_BUILD_ROOT%{_datadir}/qtmame
%endif

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

%if %{with svga}
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

%if %{with qt}
%files qtmame
%defattr(644,root,root,755)
%doc %{qtmame}-%{qtmame_ver}/{AUTHORS,README,README-us,TODO,qtmame/docs/en/*.html}
%attr(755,root,root) %{_bindir}/qtmame
%{_datadir}/qtmame
%{_pixmapsdir}/*
%{_applnkdir}/Games/Arcade/%{name}-qtmame.desktop
%endif

%files xmess-x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmess.x11

%files xmess-SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmess.SDL

%if %{with svga}
%files xmess-svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmess.svgalib
%endif
