#
# Conditional build:
%bcond_without	tests	# make check
#
Summary:	Qt Chooser - a wrapper used to select between Qt development binary versions
Summary(pl.UTF-8):	Qt Chooser - wrapper do wyboru wersji binariów programistycznych Qt
Name:		qtchooser
Version:	39
%define	githash	g4717841
Release:	2
License:	LGPL v2.1 with Digia Qt LGPL Exception v1.1 or GPL v3
Group:		Development/Tools
Source0:	http://macieira.org/qtchooser/%{name}-%{version}-%{githash}.tar.gz
# Source0-md5:	fcf1b5e8373147e48ce72b9c1ffe3d10
URL:		http://macieira.org/qtchooser/
%{?with_tests:BuildRequires:	QtCore-devel >= 4}
%{?with_tests:BuildRequires:	QtTest-devel >= 4}
BuildRequires:	libstdc++-devel
%{?with_tests:BuildRequires:	qt4-build >= 4}
%{?with_tests:BuildRequires:	qt4-qmake >= 4}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt is a cross-platform C++ application framework. Qt's primary feature
is its rich set of widgets that provide standard GUI functionality.

The Qt Chooser provides a wrapper to switch between versions of Qt
development binaries when multiple versions like 4 and 5 are installed
or local Qt builds are to be used.

In order to use Qt Chooser, include its directory
(%{_prefix}/lib/qtchooser) in your PATH.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji C++. Główną cechą Qt jest
bogaty zestaw widgetów składających się na funkcjonalność GUI.

Qt Chooser udostępnia wrapper, pozwalający na przełączanie między
wersjami binariów programistycznych Qt w przypadku, kiedy
zainstalowane jest wiele wersji (np. 4 i 5), albo ma być używana
lokalnie zbudowana wersja Qt.

Aby używać Qt Choosera, należy umieścić jego katalog
(%{_prefix}/lib/qtchooser) w zmiennej PATH.

%prep
%setup -q -n %{name}-%{version}-%{githash}

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LFLAGS="%{rpmldflags}"

%if %{with tests}
PATH="%{_libdir}/qt4/bin:$PATH" \
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

# install to alternative directory to:
# - not make it obligatory (users can opt-in)
# - avoid conflict with qt3 binaries

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	bindir=%{_prefix}/lib/qtchooser

install -d $RPM_BUILD_ROOT/etc/xdg/qtchooser

## env vars
#QT_SELECT
#QTCHOOSER_RUNTOOL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LGPL_EXCEPTION.txt
%dir /etc/xdg/qtchooser
%dir %{_prefix}/lib/qtchooser
%attr(755,root,root) %{_prefix}/lib/qtchooser/qtchooser
%attr(755,root,root) %{_prefix}/lib/qtchooser/assistant
%attr(755,root,root) %{_prefix}/lib/qtchooser/designer
%attr(755,root,root) %{_prefix}/lib/qtchooser/lconvert
%attr(755,root,root) %{_prefix}/lib/qtchooser/linguist
%attr(755,root,root) %{_prefix}/lib/qtchooser/lrelease
%attr(755,root,root) %{_prefix}/lib/qtchooser/lupdate
%attr(755,root,root) %{_prefix}/lib/qtchooser/moc
%attr(755,root,root) %{_prefix}/lib/qtchooser/pixeltool
%attr(755,root,root) %{_prefix}/lib/qtchooser/qcollectiongenerator
%attr(755,root,root) %{_prefix}/lib/qtchooser/qdbus
%attr(755,root,root) %{_prefix}/lib/qtchooser/qdbuscpp2xml
%attr(755,root,root) %{_prefix}/lib/qtchooser/qdbusviewer
%attr(755,root,root) %{_prefix}/lib/qtchooser/qdbusxml2cpp
%attr(755,root,root) %{_prefix}/lib/qtchooser/qdoc
%attr(755,root,root) %{_prefix}/lib/qtchooser/qdoc3
%attr(755,root,root) %{_prefix}/lib/qtchooser/qglinfo
%attr(755,root,root) %{_prefix}/lib/qtchooser/qhelpconverter
%attr(755,root,root) %{_prefix}/lib/qtchooser/qhelpgenerator
%attr(755,root,root) %{_prefix}/lib/qtchooser/qmake
%attr(755,root,root) %{_prefix}/lib/qtchooser/qml
%attr(755,root,root) %{_prefix}/lib/qtchooser/qml1plugindump
%attr(755,root,root) %{_prefix}/lib/qtchooser/qmlbundle
%attr(755,root,root) %{_prefix}/lib/qtchooser/qmlmin
%attr(755,root,root) %{_prefix}/lib/qtchooser/qmlplugindump
%attr(755,root,root) %{_prefix}/lib/qtchooser/qmlprofiler
%attr(755,root,root) %{_prefix}/lib/qtchooser/qmlscene
%attr(755,root,root) %{_prefix}/lib/qtchooser/qmltestrunner
%attr(755,root,root) %{_prefix}/lib/qtchooser/qmlviewer
%attr(755,root,root) %{_prefix}/lib/qtchooser/qtconfig
%attr(755,root,root) %{_prefix}/lib/qtchooser/rcc
%attr(755,root,root) %{_prefix}/lib/qtchooser/uic
%attr(755,root,root) %{_prefix}/lib/qtchooser/uic3
%attr(755,root,root) %{_prefix}/lib/qtchooser/xmlpatterns
%attr(755,root,root) %{_prefix}/lib/qtchooser/xmlpatternsvalidator
