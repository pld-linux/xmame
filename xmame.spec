Summary:	Unix/X11 port of M.A.M.E. - arcade machine emulator
Summary(es):	X-Mame Arcade Game Emulator
Summary(ko):	X������ �ý����� ���� ���ҿ� ���ӱ� ����������
Summary(pl):	Port emulatora M.A.M.E. dzia�aj�cy w �rodowisku Unix/X11
Summary(pt_BR):	Emulador de Arcades X-Mame
Name:		xmame
Version:	0.60.1
Release:	0.1
License:	GPL
Group:		Applications/Emulators
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.png
Source2:	%{name}-SDL.desktop
Source3:	%{name}-x11.desktop
Patch0:		%{name}-noattr.patch
URL:		http://x.mame.net/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	alsa-driver-devel
%ifarch %{ix86} alpha
BuildRequires:	svgalib-devel
%endif
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
emulator Mame na maszynach uniksowych z X11R6 Window System (a tak�e
linuksowych z SVGAlibem).

Mame to emulator maszyny wirtualnej: zawiera emulatory Z80, 6502,
68000 i ostatnie I86, po��czone z r�nymi emulatorami sprz�tu do gier.
Ka�dy emulator zawiera pe�ny opis sprz�tu, mapy pami�ci, obrazu,
d�wi�ku itp., co pozwala gra� w gry pod warunkiem posiadania
oryginalnych obraz�w ROM.

%description -l pt_BR
X-Mame � o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator dispon�vel em m�quinas *ix usando o sistema X-Window
X11R6 (e sobre Linux usando SVGAlib tamb�m). Mame � uma emulador de
m�quinas virtuais: ele inclui um Z80, 6502, 68000 e recentemente
microprocessadores I86, agregando uma grande quantidade de m�quinas de
arcade. Cada emulador cont�m uma descri��o sobre o hardware, mapas de
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
emulator Mame na maszynach uniksowych z X11R6 Window System (a tak�e
linuksowych z SVGAlibem).

Mame to emulator maszyny wirtualnej: zawiera emulatory Z80, 6502,
68000 i ostatnie I86, po��czone z r�nymi emulatorami sprz�tu do gier.
Ka�dy emulator zawiera pe�ny opis sprz�tu, mapy pami�ci, obrazu,
d�wi�ku itp., co pozwala gra� w gry pod warunkiem posiadania
oryginalnych obraz�w ROM.

Ten pakiet zawiera podstawowe, wsp�lne pliki XMame, potrzebne do
uruchamiania ka�dej wersji emulatora.

%package SDL
Summary:	XMame with SDL graphic output
Summary(es):	X-Mame Arcade Game Emulator - SDL
Summary(pl):	XMame z wyj�ciem graficznym SDL
Summary(pt_BR):	Emulador de Arcades X-Mame - SDL
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description SDL
This package has XMame binaries compiled for SDL graphics output.

%description SDL -l pl
Ten pakiet zawiera binaria XMame z wyj�ciem grafiki przez SDL.

%description SDL -l pt_BR
X-Mame � o porte para UNIX/X11 do projeto Mame. Ele torna o Mame
arcade emulator dispon�vel em m�quinas *ix usando o sistema X-Window
X11R6 (e sobre Linux usando SVGAlib tamb�m).

%package svgalib
Summary:	XMame - svgalib version
Summary(es):	X-Mame Arcade Game Emulator - svgalib
Summary(pl):	XMame - wersja z wyj�ciem svgalib
Summary(pt_BR):	Emulador de Arcades X-Mame - svgalib
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description svgalib
This package has XMame binaries compiled for svgalib graphic output.

%description svgalib -l pl
Ten pakiet zawiera binaria XMame z wyj�ciem grafiki przez SVGAlib.

%description svgalib -l pt_BR
X-Mame � o porte para SVGAlib do projeto Mame.

%package X11
Summary:	XMame - X11 version
Summary(es):	X-Mame Arcade Game Emulator - X11
Summary(pl):	XMame - wersja z wyj�ciem X11
Summary(pt_BR):	Emulador de Arcades X-Mame - X11
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description X11
This package has XMame binaries compiled for X11 graphic output.

%description X11 -l pl
Ten pakiet zawiera binaria XMame z wyj�ciem grafiki pod X11.

%description X11 -l pt_BR
X-Mame � o porte para UNIX/X11 do projeto Mame.

%package screensaver
Summary:	XMame - screensaver
Summary(pl):	XMame - wygaszacz ekranu
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description screensaver
The XMame screensaver.

%description screensaver -l pl
Wygaszacz ekranu XMame.

%prep
%setup -q
%patch0 -p1

%build

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
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games/Arcade}

install xmame.SDL $RPM_BUILD_ROOT%{_bindir}
%ifarch %{ix86} alpha
install xmame.svgalib $RPM_BUILD_ROOT%{_bindir}
%endif
install xmame.x11 $RPM_BUILD_ROOT%{_bindir}
install contrib/tools/xmame-screensaver $RPM_BUILD_ROOT%{_bindir}

make -f makefile.unix XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name} copycab

install src/unix/doc/xmame.6 $RPM_BUILD_ROOT%{_mandir}/man6

install %{SOURCE1}		$RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} %{SOURCE3}	$RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc doc/*
%{_mandir}/man6/*
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/cab
%dir %{_datadir}/games/%{name}/rc
%{_datadir}/games/%{name}/cab/*
%{_pixmapsdir}/xmame.png

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}.SDL
%{_applnkdir}/Games/Arcade/%{name}-SDL.desktop

%ifarch %{ix86} alpha
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}.svgalib
%endif

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}.x11
%{_applnkdir}/Games/Arcade/%{name}-x11.desktop

%files screensaver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmame-screensaver
