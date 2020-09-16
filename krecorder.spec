%define snapshot 20200916
%define commit f5f31989e23559cdb5739cea8af8c82f74b67254

Name:		krecorder
Version:	0.0.1
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Video player for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/krecorder/-/archive/master/krecorder-master.tar.bz2
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
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)

%description
Audio recorder for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-master
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/krecorder
%{_datadir}/applications/org.kde.krecorder.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.krecorder.svg
%{_datadir}/metainfo/org.kde.krecorder.appdata.xml
