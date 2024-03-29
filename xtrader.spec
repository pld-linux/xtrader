Summary:	XTrader - a technical stock analysis program
Summary(pl.UTF-8):	Xtrader - program do analizy technicznej giełdy
Name:		xtrader
Version:	0.99.9
Release:	0.1
License:	QPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xtrader/%{name}-%{version}.tar.gz
# Source0-md5:	c15cb947194a6c405b3ef5d2fe916793
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://xtrader.sourceforge.net/
BuildRequires:	fltk-devel 
BuildRequires:	ptypes-devel >= 1.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XTrader is a technical analysis program for financial instruments.
There is a simple portfolio module where you can edit transactions,
create reports and charts.

%description -l pl.UTF-8
XTrader to program do technicznej analizy instrumentów finansowych.
Zawiera prosty moduł portfolio, gdzie można modyfikować transakcje,
tworzyć raporty i wykresy.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} -f Makefile.linux \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install xtrader $RPM_BUILD_ROOT%{_bindir}
install xtrader_32x32.png $RPM_BUILD_ROOT%{_pixmapsdir}/xtrader.png

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
