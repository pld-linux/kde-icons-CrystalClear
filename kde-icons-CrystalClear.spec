%define		_name	CrystalClear
Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	0.1
Release:	1
License:	LGPL
Group:		Themes
Source0:	http://linuxcult.com/crystal/icons/%{_name}.tar.gz
# Source0-md5:	adb7962b585c8ad12adc3b82246edb35
URL:		http://www.everaldo.com/
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is icons theme for KDE.

%description -l pl
%{_name} to motyw ikon dla KDE.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
