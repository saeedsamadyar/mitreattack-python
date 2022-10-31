from mitreattack.stix20 import MitreAttackData

def main():
    mitre_attack_data = MitreAttackData("path/to/enterprise-attack.json")

    software_used_by_campaigns = mitre_attack_data.get_software_used_by_campaigns()
    print(f"Software used by campaigns ({len(software_used_by_campaigns.keys())}):")
    for id, software_used in software_used_by_campaigns.items():
        print(f"* {id} - {len(software_used)} software used")


if __name__ == "__main__":
    main()