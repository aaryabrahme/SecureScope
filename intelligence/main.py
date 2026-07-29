from intelligence.aggregator import (
    create_security_report
)


def main():

    report = create_security_report()

    print()
    print("SecureScope unified intelligence report generated")

    print(
        report
    )



if __name__ == "__main__":
    main()
