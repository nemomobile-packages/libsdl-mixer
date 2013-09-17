Summary: Simple DirectMedia Layer - Sample Mixer Library
Name: SDL2_mixer
Version: 2.0.0
Release: 2
Source: http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz
URL: http://www.libsdl.org/projects/SDL_mixer/
License: zlib
Group: Applications/Multimedia
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(flac)
BuildRequires: smpeg-devel

%description
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis,
Tremor, SMPEG MP3, and libmad MP3 libraries.

%package devel
Summary: Simple DirectMedia Layer - Sampler Mixer Library (Development)
Group: Development/Libraries
Requires: %{name}

%description devel
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis,
Tremor, SMPEG MP3, and libmad MP3 libraries.

%prep
%setup -q

%build
%configure
make

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*

