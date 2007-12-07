%define module	Test-WWW-Mechanize
%define name	perl-%{module}
%define version 1.18
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release:	%{release} 
License:	GPL or Artistic
Group:		Development/Perl
Summary:        Testing-specific WWW::Mechanize subclass
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(HTTP::Server::Simple)
BuildRequires:  perl(Carp::Assert::More)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(URI)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(WWW::Mechanize) 
BuildRequires:  perl(HTML::Lint)
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Test::WWW::Mechanize is a subclass of WWW::Mechanize that incorporates features
for web application testing.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/man3/*

