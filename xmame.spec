#
# Conditional build:
%bcond_without	svga	# don't build svga version
%bcond_without	qt	# don't build qtmame
#
%define		qtmame		qtmame
%define		qtmame_ver	2.0.6
Summary:	Unix/X11 port of M.A.M.E. - arcade machine emulator
Summary(es.UTF-8):	X-Mame Arcade Game Emulator
Summary(ko.UTF-8):	X윈도우 시스템을 위한 업소용 게임기 에물레이터
Summary(pl.UTF-8):	Port emulatora M.A.M.E. działający w środowisku Unix/X11
Summary(pt_BR.UTF-8):	Emulador de Arcades X-Mame
Name:		xmame
Version:	0.106
Release:	0.1
License:	GPL
Group:		Applications/Emulators
#Source0Download:	http://x.mame.net/xmame-doc-7.html
Source0:	http://x.mame.net/download/%{name}-%{version}.tar.bz2
# Source0-md5:	b2b18d32a03ebd4d9c9476fbb93695ca
Source1:	http://lecha.homelinux.com/ingenio/archivos/%{qtmame}-%{qtmame_ver}.tar.gz
# Source1-md5:	69b568b8e68877a11b2ffa4845829bb1
Source2:	%{name}-SDL.desktop
Source3:	%{name}-x11.desktop
Source4:	%{name}.png
Source5:	%{name}-qtmame.desktop
Source6:	%{name}-qtmame_pl.ts
Source7:	http://x.mame.net/download/%{name}-doc.pdf
# Source7-md5:	f4a7b59d020ce35decd03b67639639a2
URL:		http://x.mame.net/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	alsa-driver-devel >= 0.9
BuildRequires:	artsc-devel
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	libusb-devel
%{?with_qt:BuildRequires:	qt-devel >= 1:3.0}
%{?with_qt:BuildRequires:	qt-linguist >= 3.0}
%{?with_svga:BuildRequires:	svgalib-devel}
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

%description -l pl.UTF-8
XMame to uniksowy/X-owy port projektu Mame. Pozwala uruchamiać
emulator Mame na maszynach uniksowych z X11R6 Window System (a także
linuksowych z SVGAlibem).

Mame to emulator maszyny wirtualnej: zawiera emulatory Z80, 6502,
68000 i ostatnie I86, połączone z różnymi emulatorami sprzętu do gier.
Każdy emulator zawiera pełny opis sprzętu, mapy pamięci, obrazu,
dźwięku itp., co pozwala grać w gry pod warunkiem posiadania
oryginalnych obrazów ROM.

%description -l pt_BR.UTF-8
X-Mame é o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator disponível em máquinas *ix usando o sistema X-Window
X11R6 (e sobre Linux usando SVGAlib também). Mame é uma emulador de
máquinas virtuais: ele inclui um Z80, 6502, 68000 e recentemente
microprocessadores I86, agregando uma grande quantidade de máquinas de
arcade. Cada emulador contém uma descrição sobre o hardware, mapas de
memória, vídeo, som, etc, tornando possível que você possa jogar suas
ROMS originais.

%package common
Summary:	XMame - common files
Summary(pl.UTF-8):	XMame - wspólne pliki
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

%description common -l pl.UTF-8
XMame to uniksowy/X-owy port projektu Mame. Pozwala uruchamiać
emulator Mame na maszynach uniksowych z X11R6 Window System (a także
linuksowych z SVGAlibem).

Mame to emulator maszyny wirtualnej: zawiera emulatory Z80, 6502,
68000 i ostatnie I86, połączone z różnymi emulatorami sprzętu do gier.
Każdy emulator zawiera pełny opis sprzętu, mapy pamięci, obrazu,
dźwięku itp., co pozwala grać w gry pod warunkiem posiadania
oryginalnych obrazów ROM.

Ten pakiet zawiera podstawowe, wspólne pliki XMame, potrzebne do
uruchamiania każdej wersji emulatora.

%package SDL
Summary:	XMame with SDL graphic output
Summary(es.UTF-8):	XMame Arcade Game Emulator - SDL
Summary(pl.UTF-8):	XMame z wyjściem graficznym SDL
Summary(pt_BR.UTF-8):	Emulador de Arcades XMame - SDL
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description SDL
This package has XMame binaries compiled for SDL graphics output.

%description SDL -l pl.UTF-8
Ten pakiet zawiera binaria XMame z wyjściem grafiki przez SDL.

%description SDL -l pt_BR.UTF-8
XMame é o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator disponível em máquinas *ix usando o sistema X-Window
X11R6 (e sobre Linux usando SVGAlib também).

%package svgalib
Summary:	XMame - svgalib version
Summary(es.UTF-8):	XMame Arcade Game Emulator - svgalib
Summary(pl.UTF-8):	XMame - wersja z wyjściem svgalib
Summary(pt_BR.UTF-8):	Emulador de Arcades XMame - svgalib
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description svgalib
This package has XMame binaries compiled for svgalib graphic output.

%description svgalib -l pl.UTF-8
Ten pakiet zawiera binaria XMame z wyjściem grafiki przez SVGAlib.

%description svgalib -l pt_BR.UTF-8
XMame é o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator disponível em máquinas *ix usando o sistema X11 (e
sobre Linux usando SVGAlib também).

%package x11
Summary:	XMame - x11 version
Summary(es.UTF-8):	XMame Arcade Game Emulator - X11
Summary(pl.UTF-8):	XMame - wersja z wyjściem x11
Summary(pt_BR.UTF-8):	Emulador de Arcades XMame - X11
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description x11
This package has XMame binaries compiled for x11 graphic output.

%description x11 -l pl.UTF-8
Ten pakiet zawiera binaria XMame z wyjściem grafiki pod X11.

%description x11 -l pt_BR.UTF-8
XMame é o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator disponível em máquinas *ix usando o sistema X-Window
X11R6 (e sobre Linux usando SVGAlib também).

%package screensaver
Summary:	XMame - screensaver
Summary(pl.UTF-8):	XMame - wygaszacz ekranu
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description screensaver
The XMame screensaver.

%description screensaver -l pl.UTF-8
Wygaszacz ekranu XMame.

%package qtmame
Summary:	Qtmame - graphic interface for XMame
Summary(pl.UTF-8):	Qtmame - graficzny interfejs dla XMame
Group:		Applications/Emulators
URL:		http://move.to/ingenio
Requires:	%{name}-common = %{version}-%{release}
Provides:	qtmame
Obsoletes:	qtmame

%description qtmame
Graphic interface for XMame.

%description qtmame -l pl.UTF-8
Graficzny interfejs dla XMame.

%package xmess-x11
Summary:	xmess - a virtual machine emulator for x11
Summary(pl.UTF-8):	xmess - emulator maszyny wirtualnej dla x11
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description xmess-x11
Mess is just like mame - a virtual machine emulator, only it
doesn't emulate arcade machines but rather computers and consoles.
This package contains binaries for x11.

%description xmess-x11 -l pl.UTF-8
Mess to to samo co mame - emulator maszyny wirtualnej, tyle że
nie emuluje on automatów arcade'owych a komputery i konsole.
Ten pakiet zawiera binaria dla x11.

%package xmess-SDL
Summary:	xmess - a virtual machine emulator for SDL
Summary(pl.UTF-8):	xmess - emulator maszyny wirtualnej dla SDL
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description xmess-SDL
Mess is just like mame - a virtual machine emulator, only it
doesn't emulate arcade machines but rather computers and consoles.
This package contains binaries for SDL.

%description xmess-SDL -l pl.UTF-8
Mess to to samo co mame - emulator maszyny wirtualnej, tyle że
nie emuluje on automatów arcade'owych a komputery i konsole.
Ten pakiet zawiera binaria dla SDL.

%package xmess-svgalib
Summary:	xmess - a virtual machine emulator for svgalib
Summary(pl.UTF-8):	xmess - emulator maszyny wirtualnej dla svgalib
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description xmess-svgalib
Mess is just like mame - a virtual machine emulator, only it
doesn't emulate arcade machines but rather computers and consoles.
This package contains binaries for svgalib.

%description xmess-svgalib -l pl.UTF-8
Mess to to samo co mame - emulator maszyny wirtualnej, tyle że
nie emuluje on automatów arcade'owych a komputery i konsole.
Ten pakiet zawiera binaria dla svgalib.

%prep
%setup -q -a1
install %{SOURCE7} doc/
%if %{with qt}
install %{_datadir}/automake/config.* %{qtmame}-%{qtmame_ver}/admin
install %{SOURCE6} %{qtmame}-%{qtmame_ver}/qtmame/qtmame_pl.ts
lrelease %{qtmame}-%{qtmame_ver}/qtmame/qtmame.pro
%endif

%build
%ifnarch %{ix86}
sed -i -e 's/^\(X86_ASM\)/# \1/' makefile.mame
sed -i -e 's/^\(MY_CPU = i386\)/# \1/' makefile.unix
%endif

%if %{with qt}
cd %{qtmame}-%{qtmame_ver}
%configure2_13

%{__make}

cd ..
%endif

%{__make} -f makefile.unix \
	TARGET=mess \
	PREFIX=%{_prefix} \
	XMAMEROOT=%{_datadir}/games/%{name} \
	CC="%{__cc}" \
	LD="%{__cc} %{rpmldflags}" \
	DISPLAY_METHOD=SDL \
	SOUND_ESOUND=1 \
	SOUND_ALSA=1 \
	SOUND_ARTS_TEIRA=1 \
	SOUND_ARTS_SMOTEK=1 \
	SOUND_SDL=1 \
	#XMAME_NET=1

%{__make} -f makefile.unix \
	TARGET=mess \
	PREFIX=%{_prefix} \
	XMAMEROOT=%{_datadir}/games/%{name} \
	CC="%{__cc}" \
	LD="%{__cc} %{rpmldflags}" \
	X11LIB="-L/usr/X11R6/%{_lib}" \
	DISPLAY_METHOD=x11 \
	SOUND_ESOUND=1 \
	SOUND_ALSA=1 \
	SOUND_ARTS_TEIRA=1 \
	SOUND_ARTS_SMOTEK=1 \
	SOUND_SDL=1 \
	#XMAME_NET=1

%if %{with svga}
%{__make} -f makefile.unix \
	TARGET=mess \
	PREFIX=%{_prefix} \
	XMAMEROOT=%{_datadir}/games/%{name} \
	CC="%{__cc}" \
	LD="%{__cc} %{rpmldflags}" \
	DISPLAY_METHOD=svgalib \
	SOUND_ESOUND=1 \
	SOUND_ALSA=1 \
	SOUND_ARTS_TEIRA=1 \
	SOUND_ARTS_SMOTEK=1 \
	SOUND_SDL=1 \
	#XMAME_NET=1
%endif

%{__make} -f makefile.unix \
	PREFIX=%{_prefix} \
	XMAMEROOT=%{_datadir}/games/%{name} \
	CC="%{__cc}" \
	LD="%{__cc} %{rpmldflags}" \
	DISPLAY_METHOD=SDL \
	SOUND_ESOUND=1 \
	SOUND_ALSA=1 \
	SOUND_ARTS_TEIRA=1 \
	SOUND_ARTS_SMOTEK=1 \
	SOUND_SDL=1 \
	#XMAME_NET=1

%if %{with svga}
%{__make} -f makefile.unix \
	PREFIX=%{_prefix} \
	XMAMEROOT=%{_datadir}/games/%{name} \
	CC="%{__cc}" \
	LD="%{__cc} %{rpmldflags}" \
	DISPLAY_METHOD=svgalib \
	SOUND_ESOUND=1 \
	SOUND_ALSA=1 \
	SOUND_ARTS_TEIRA=1 \
	SOUND_ARTS_SMOTEK=1 \
	SOUND_SDL=1 \
	#XMAME_NET=1
%endif

%{__make} -f makefile.unix \
	PREFIX=%{_prefix} \
	XMAMEROOT=%{_datadir}/games/%{name} \
	CC="%{__cc}" \
	LD="%{__cc} %{rpmldflags}" \
	X11LIB="-L/usr/X11R6/%{_lib}" \
	DISPLAY_METHOD=x11 \
	SOUND_ESOUND=1 \
	SOUND_ALSA=1 \
	SOUND_ARTS_TEIRA=1 \
	SOUND_ARTS_SMOTEK=1 \
	SOUND_SDL=1 \
	#XMAME_NET=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6} \
	$RPM_BUILD_ROOT%{_datadir}/games/%{name}/{cab,rc} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}} \
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
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}

%if %{with qt}
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}

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
%{_desktopdir}/%{name}-SDL.desktop

%if %{with svga}
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}.svgalib
%endif

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}.x11
%{_desktopdir}/%{name}-x11.desktop

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
%{_desktopdir}/%{name}-qtmame.desktop
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
