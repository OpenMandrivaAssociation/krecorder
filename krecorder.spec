%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

#define git 20200916
%define commit f5f31989e23559cdb5739cea8af8c82f74b67254

Name:		krecorder
Version:	23.08.3
Release:	%{?git:0.%{git}.}1
Summary:	Video player for Plasma Mobile
%if %{defined git}
Source0:	https://invent.kde.org/plasma-mobile/krecorder/-/archive/master/krecorder-master.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5KirigamiAddons)

%description
Audio recorder for Plasma Mobile

%prep
%autosetup -p1 %{?git:-n %{name}-master}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/krecorder
%{_datadir}/applications/org.kde.krecorder.desktop
%{_datadir}/metainfo/org.kde.krecorder.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.krecorder.svg
