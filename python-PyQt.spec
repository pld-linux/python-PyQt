%define		module	PyQt
Summary:	Python bindings for the Qt toolkit
Summary(pl):	Dowi±zania do toolkitu Qt dla Pythona
Summary(ko):	QtÀÇ ÆÄÀÌ½ã ¸ðµâ
Name:		python-%{module}
Version:	3.13
#%%define		_snap		20040226
#%Release:	0.%{_snap}.2
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://www.river-bank.demon.co.uk/download/PyQt/PyQt-x11-gpl-%{version}.tar.gz
# Source0-md5:	a4145b39742a4d9df9b6bf06495f75f5
# Source0:	http://www.river-bank.demon.co.uk/download/snapshots/PyQt/PyQt-x11-gpl-snapshot-%{_snap}.tar.gz
URL:		http://www.riverbankcomputing.co.uk/pyqt/index.php
BuildRequires:	OpenGL-devel
BuildRequires:	python-devel >= 2.2.2
BuildRequires:	qscintilla-devel >= 1:1.2
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	rpm-pythonprov
BuildRequires:	sip >= 2:4.1.1
#%%requires_eq	sip
Requires:	sip >= 2:4.1.1
%pyrequires_eq	python
Requires:	OpenGL
Requires:	qscintilla >= 1:1.4
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define         _sipfilesdir	%{_datadir}/sip

%description
PyQt is a set of Python bindings for the Qt toolkit. The bindings are
implemented as a set of Python modules: qt, qtcanvas, qtgl, qtnetwork,
qtsql, qttable and qtxml, and contains 300 classes and over 5,750
functions and methods.

%description -l pl
PyQT to zbiór dowi±zañ do Qt dla Pythona. Dowi±zania zosta³y
zaimplementowane jako modu³y Pythona: qt, qtcanvas, qtgl, qtnetwork,
qtsql, qttable i qtxml - zawieraj± one 300 klas i ponad 5 750 funkcji
i metod.

%package devel
Summary:	Files needed to build other bindings based on Qt
Summary(pl):	Pliki potrzebne do budowania innych dowi±zañ bazowanych na Qt
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	sip >= 2:3.10.2

%description devel
Files needed to build other bindings for C++ classes that inherit from
any of the Qt classes (e.g. KDE or your own).

%description devel -l pl
Pliki potrzebne do budowania innych dowi±zañ do klas C++
dziedzicz±cych z dowolnej klasy Qt (np. KDE lub w³asnych).

%package examples
Summary:	Examples for PyQt
Summary(pl):	Przyklady do PyQt
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples code demonstrating how to use the Python bindings for Qt.

%description examples -l pl
Przykladowy kod demonstruj±cy jak u¿ywaæ PyQT.

%prep
%setup -q -n %{module}-x11-gpl-%{version}
#%%setup -q -n %{module}-x11-gpl-snapshot-%{_snap}

%build
echo 'yes' | python configure.py \
	-c -j 3 \
	-b %{_bindir} \
	-n %{_includedir}/qt \
	-o %{_libdir} \
	-d %{py_sitedir} \
	-v %{_sipfilesdir}

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -fPIC -pipe -w -D_REENTRANT" \
	LINK="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/python/%{module},%{_sipfilesdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
cp -R examples3/* $RPM_BUILD_ROOT%{_examplesdir}/python/%{module}

cp -R sip/* $RPM_BUILD_ROOT%{_sipfilesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS doc/PyQt.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/*.so*
%{py_sitedir}/*.py[co]

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/pyqt*.sip
%dir %{_sipfilesdir}/qt*
%{_sipfilesdir}/qt*/*.sip

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/python/%{module}
