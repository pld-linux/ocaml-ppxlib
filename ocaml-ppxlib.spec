#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	ppxlib - meta-programming for OCaml
Summary(pl.UTF-8):	ppxlib - metaprogramowanie dla OCamla
Name:		ocaml-ppxlib
Version:	0.38.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/ocaml-ppx/ppxlib/releases
Source0:	https://github.com/ocaml-ppx/ppxlib/releases/download/%{version}/ppxlib-%{version}.tbz
# Source0-md5:	1db22b0a6dd8a590f3593628ead2f1fd
Patch0:		%{name}-stdlib-shims.patch
URL:		https://github.com/ocaml-ppx/ppxlib
BuildRequires:	ocaml >= 1:4.04.1
BuildRequires:	ocaml-cmdliner-devel
BuildRequires:	ocaml-dune >= 2.7
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-ocaml-compiler-libs-devel >= 0.11.0
BuildRequires:	ocaml-ppx_derivers-devel >= 1.0
BuildRequires:	ocaml-re-devel
BuildRequires:	ocaml-sexplib0-devel >= 0.12
BuildRequires:	ocaml-yojson-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Ppxlib is the standard library for ppx rewriters and other programs
that manipulate the in-memory representation of OCaml programs, a.k.a
the "Parsetree".

This package contains files needed to run bytecode executables using
ppxlib library.

%description -l pl.UTF-8
Ppxlib to standardowa biblioteka do funkcji przepisujących ppx i
innych programów modyfikujących reprezentację w pamięci programów
ocamlowych, tzw. "parsetree" (drzewo analizy).

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppxlib.

%package devel
Summary:	ppxlib - meta-programming for OCaml - development part
Summary(pl.UTF-8):	ppxlib - metaprogramowanie dla OCamla - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
ppxlib library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppxlib.

%prep
%setup -q -n ppxlib-%{version}
%patch -P0 -p1

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppxlib/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppxlib/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ppxlib*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md HISTORY.md LICENSE.md README.md
%attr(755,root,root) %{_bindir}/ppxlib-pp-ast
%dir %{_libdir}/ocaml/ppxlib
%{_libdir}/ocaml/ppxlib/META
%{_libdir}/ocaml/ppxlib/*.cma
%dir %{_libdir}/ocaml/ppxlib/ast
%{_libdir}/ocaml/ppxlib/ast/*.cma
%dir %{_libdir}/ocaml/ppxlib/astlib
%{_libdir}/ocaml/ppxlib/astlib/*.cma
%dir %{_libdir}/ocaml/ppxlib/metaquot
%{_libdir}/ocaml/ppxlib/metaquot/*.cma
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/metaquot/ppx.exe
%dir %{_libdir}/ocaml/ppxlib/metaquot_lifters
%{_libdir}/ocaml/ppxlib/metaquot_lifters/*.cma
%dir %{_libdir}/ocaml/ppxlib/print_diff
%{_libdir}/ocaml/ppxlib/print_diff/*.cma
%dir %{_libdir}/ocaml/ppxlib/runner
%{_libdir}/ocaml/ppxlib/runner/*.cma
%dir %{_libdir}/ocaml/ppxlib/runner_as_ppx
%{_libdir}/ocaml/ppxlib/runner_as_ppx/*.cma
%dir %{_libdir}/ocaml/ppxlib/stdppx
%{_libdir}/ocaml/ppxlib/stdppx/*.cma
%dir %{_libdir}/ocaml/ppxlib/traverse
%{_libdir}/ocaml/ppxlib/traverse/*.cma
%dir %{_libdir}/ocaml/ppxlib/traverse_builtins
%{_libdir}/ocaml/ppxlib/traverse_builtins/*.cma
%dir %{_libdir}/ocaml/ppxlib/__private__
%dir %{_libdir}/ocaml/ppxlib/__private__/ppx_foo_deriver
%{_libdir}/ocaml/ppxlib/__private__/ppx_foo_deriver/*.cma
%dir %{_libdir}/ocaml/ppxlib-bench
%{_libdir}/ocaml/ppxlib-bench/META
%dir %{_libdir}/ocaml/ppxlib-tools
%{_libdir}/ocaml/ppxlib-tools/META
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/ast/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/astlib/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/metaquot/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/metaquot_lifters/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/print_diff/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/runner/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/runner_as_ppx/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/stdppx/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/traverse/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppxlib/traverse_builtins/*.cmxs
%{_libdir}/ocaml/ppxlib/__private__/ppx_foo_deriver/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppxlib/*.cmi
%{_libdir}/ocaml/ppxlib/*.cmt
%{_libdir}/ocaml/ppxlib/*.cmti
%{_libdir}/ocaml/ppxlib/*.mli
%{_libdir}/ocaml/ppxlib/ast/*.cmi
%{_libdir}/ocaml/ppxlib/ast/*.cmt
%{_libdir}/ocaml/ppxlib/ast/*.cmti
%{_libdir}/ocaml/ppxlib/ast/*.mli
%{_libdir}/ocaml/ppxlib/astlib/*.cmi
%{_libdir}/ocaml/ppxlib/astlib/*.cmt
%{_libdir}/ocaml/ppxlib/astlib/*.cmti
%{_libdir}/ocaml/ppxlib/astlib/*.mli
%{_libdir}/ocaml/ppxlib/metaquot/*.cmi
%{_libdir}/ocaml/ppxlib/metaquot/*.cmt
%{_libdir}/ocaml/ppxlib/metaquot_lifters/*.cmi
%{_libdir}/ocaml/ppxlib/metaquot_lifters/*.cmt
%{_libdir}/ocaml/ppxlib/print_diff/*.cmi
%{_libdir}/ocaml/ppxlib/print_diff/*.cmt
%{_libdir}/ocaml/ppxlib/print_diff/*.cmti
%{_libdir}/ocaml/ppxlib/print_diff/*.mli
%{_libdir}/ocaml/ppxlib/runner/*.cmi
%{_libdir}/ocaml/ppxlib/runner/*.cmt
%{_libdir}/ocaml/ppxlib/runner_as_ppx/*.cmi
%{_libdir}/ocaml/ppxlib/runner_as_ppx/*.cmt
%{_libdir}/ocaml/ppxlib/stdppx/*.cmi
%{_libdir}/ocaml/ppxlib/stdppx/*.cmt
%{_libdir}/ocaml/ppxlib/traverse/*.cmi
%{_libdir}/ocaml/ppxlib/traverse/*.cmt
%{_libdir}/ocaml/ppxlib/traverse_builtins/*.cmi
%{_libdir}/ocaml/ppxlib/traverse_builtins/*.cmt
%{_libdir}/ocaml/ppxlib/__private__/ppx_foo_deriver/.public_cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppxlib/*.a
%{_libdir}/ocaml/ppxlib/*.cmx
%{_libdir}/ocaml/ppxlib/*.cmxa
%{_libdir}/ocaml/ppxlib/ast/*.a
%{_libdir}/ocaml/ppxlib/ast/*.cmx
%{_libdir}/ocaml/ppxlib/ast/*.cmxa
%{_libdir}/ocaml/ppxlib/astlib/*.a
%{_libdir}/ocaml/ppxlib/astlib/*.cmx
%{_libdir}/ocaml/ppxlib/astlib/*.cmxa
%{_libdir}/ocaml/ppxlib/metaquot/*.a
%{_libdir}/ocaml/ppxlib/metaquot/*.cmx
%{_libdir}/ocaml/ppxlib/metaquot/*.cmxa
%{_libdir}/ocaml/ppxlib/metaquot_lifters/*.a
%{_libdir}/ocaml/ppxlib/metaquot_lifters/*.cmx
%{_libdir}/ocaml/ppxlib/metaquot_lifters/*.cmxa
%{_libdir}/ocaml/ppxlib/print_diff/*.a
%{_libdir}/ocaml/ppxlib/print_diff/*.cmx
%{_libdir}/ocaml/ppxlib/print_diff/*.cmxa
%{_libdir}/ocaml/ppxlib/runner/*.a
%{_libdir}/ocaml/ppxlib/runner/*.cmx
%{_libdir}/ocaml/ppxlib/runner/*.cmxa
%{_libdir}/ocaml/ppxlib/runner_as_ppx/*.a
%{_libdir}/ocaml/ppxlib/runner_as_ppx/*.cmx
%{_libdir}/ocaml/ppxlib/runner_as_ppx/*.cmxa
%{_libdir}/ocaml/ppxlib/stdppx/*.a
%{_libdir}/ocaml/ppxlib/stdppx/*.cmx
%{_libdir}/ocaml/ppxlib/stdppx/*.cmxa
%{_libdir}/ocaml/ppxlib/traverse/*.a
%{_libdir}/ocaml/ppxlib/traverse/*.cmx
%{_libdir}/ocaml/ppxlib/traverse/*.cmxa
%{_libdir}/ocaml/ppxlib/traverse_builtins/*.a
%{_libdir}/ocaml/ppxlib/traverse_builtins/*.cmx
%{_libdir}/ocaml/ppxlib/traverse_builtins/*.cmxa
%{_libdir}/ocaml/ppxlib/__private__/ppx_foo_deriver/*.a
%{_libdir}/ocaml/ppxlib/__private__/ppx_foo_deriver/*.cmx
%{_libdir}/ocaml/ppxlib/__private__/ppx_foo_deriver/*.cmxa
%endif
%{_libdir}/ocaml/ppxlib/dune-package
%{_libdir}/ocaml/ppxlib/opam
%{_libdir}/ocaml/ppxlib-bench/dune-package
%{_libdir}/ocaml/ppxlib-bench/opam
%{_libdir}/ocaml/ppxlib-tools/dune-package
%{_libdir}/ocaml/ppxlib-tools/opam
%{_examplesdir}/%{name}-%{version}
