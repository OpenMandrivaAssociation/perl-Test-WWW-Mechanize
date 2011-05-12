%define upstream_name	 Test-WWW-Mechanize
%define upstream_version 1.32

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Testing-specific WWW::Mechanize subclass
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Carp::Assert::More)
BuildRequires:  perl(HTML::Lint)
BuildRequires:	perl(HTTP::Server::Simple)
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(URI)
BuildRequires:  perl(WWW::Mechanize) 

BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Test::WWW::Mechanize is a subclass of WWW::Mechanize that incorporates features
for web application testing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# change listening port
perl -pi -e 's/13432/17987/' t/TestServer.pm
%make test

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
