Name:           radeon-profile
Version:        20200824
Release:        1
Summary:        Application to read current clocks of ATi Radeon cards (xf86-video-ati, xf86-video-amdgpu) 
License:        GPL2.0
Group:          System/Configuration/Hardware
URL:            https://github.com/marazmista/radeon-profile
Source0:        https://github.com/marazmista/radeon-profile/archive/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  qmake5
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ninja

Requires:       glxinfo
Requires:       xdriinfo
Requires:       xrandr


%description
Application to read current clocks of ATi Radeon cards (xf86-video-ati, xf86-video-amdgpu) 

%prep
%setup -q

sed -i -e 's/TrayIcon;//' %{name}/extra/radeon-profile.desktop

%build
pushd %{name}
%qmake_qt5
%make_build
popd

%install
pushd %{name}
%make_install INSTALL_ROOT="%{buildroot}"

%files
%doc LICENSE README.md
%{_bindir}/radeon-profile
%{_datadir}/applications/radeon-profile.desktop
%{_iconsdir}/hicolor/*/apps/radeon-profile.png
#{_datadir}/radeon-profile/*.qm
