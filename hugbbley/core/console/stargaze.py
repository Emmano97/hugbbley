import argparse
from hugbbley.core.console.file_generator import create_config_file, create_sqlite_db_file
from hugbbley.core.console.tables_generator import create_tables
from hugbbley import MODULE_NAME


def main():
    parser = argparse.ArgumentParser(description=f"Command-line interface for creating {MODULE_NAME} components")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", help="Subcommand to execute")

    # Subparser for 'create' command
    parser_create = subparsers.add_parser("create", help=f"Create {MODULE_NAME} component")
    subsubparsers = parser_create.add_subparsers(title="component",
                                                 dest="component",
                                                 help="Component to execute")

    # Subparser for creating config
    parser_create_config = subsubparsers.add_parser("config", help="Create configuration")
    parser_create_config.set_defaults(func=create_config_file)

    # Subparser for creating db
    parser_create_db = subsubparsers.add_parser("db", help="Create sqlite db")
    parser_create_db.set_defaults(func=create_sqlite_db_file)

    # Subparser for creating db
    parser_create_tables = subsubparsers.add_parser("tables", help="Create db tables")
    parser_create_tables.set_defaults(func=create_tables)

    args = parser.parse_args()

    if args.subcommand == "create":
        if args.component:
            args.func(args)
        else:
            parser_create.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
