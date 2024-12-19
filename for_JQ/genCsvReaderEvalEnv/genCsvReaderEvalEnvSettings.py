"""
制約
1) 生成されるCsvReaderのノード名は"CsvReader"である。
"""
import os, sys
import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True  # ダブルクォーテーションを保持（インデントは保持されない）


def getInputComponent(data):
    """
    yamlの情報から入力元コンポのリストを取得する関数
    @in  data: yamlをloadした辞書型変数
    @out sorted(ret): ConnectedPortのコンポ名を重複なしで抽出したリスト
    """
    ret = set()
    if "InputPorts" in data:
        for input_port in data["InputPorts"]:
            if "ConnectedPort" in input_port and "Path" in input_port["ConnectedPort"]:
                input_component_name = input_port["ConnectedPort"]["Path"].split("/")[0]
                ret.add(input_component_name)
            else:
                print(
                    "Error: 'ConnectedPort'-'Path' does not exist in 'InputPorts' {} in input yaml file.".format(
                        input_port["name"]
                    )
                )
                exit(1)
    else:
        print("Error: 'InputPorts' does not exist in input yaml file.")
        exit(1)

    return sorted(ret)


def genCsvReaderGeneratorSettingYaml(
    output_path_csvreader_generator_setting_yaml, csvreader_component_name_list
):
    """
    csvreader_generatorの設定ファイルを自動生成する関数
    """
    os.makedirs(output_path_csvreader_generator_setting_yaml, exist_ok=True)

    return


def genDumpSettingIni(
    output_path_dump_setting_ini,
    csvreader_component_name_list,
    test_target_component_name,
    test_target_node_name,
):
    """
    Dump設定iniファイルを自動生成する関数
    """
    output_dir = "/".join(output_path_dump_setting_ini.split("/")[:-1])
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path_dump_setting_ini, "w") as f_out:
        # Dump取得有無の設定
        f_out.write("[hogehoge]\n")  # iniファイルのキー名
        for csvreader_component_name in csvreader_component_name_list:
            f_out.write(f"{csvreader_component_name}CsvReaderOutput=1\n")
        f_out.write(f"{test_target_component_name}{test_target_node_name}Input=1\n")
        f_out.write(f"{test_target_component_name}{test_target_node_name}Output=1\n")
        # Dumpのフレーム数の設定
        f_out.write("[hogehoge]\n")  # iniファイルのキー名
        for csvreader_component_name in csvreader_component_name_list:
            f_out.write(f"{csvreader_component_name}CsvReaderMaxFrameNum=2400\n")
        f_out.write(
            f"{test_target_component_name}{test_target_node_name}MaxFrameNum=2400\n"
        )

    return


def genLaunchYaml(
    output_path_launch_yaml,
    output_path_dump_setting_ini,
    csvreader_component_name_list,
    test_target_component_name,
    test_target_node_name,
):
    """
    Launchファイルを自動生成する関数
    """
    output_dir = "/".join(output_path_launch_yaml.split("/")[:-1])
    os.makedirs(output_dir, exist_ok=True)


if __name__ == "__main__":
    # コマンドライン引数の取得
    args = sys.argv
    if len(args) == 3:
        test_target_component_yaml = args[1]
        test_target_node_name = args[2]
    else:
        print(
            "Usage: python3 genCsvReaderEvalEnvSettings.py </path/to/test_target.component_public.yaml> <test_target_node_name>"
        )
        exit(1)

    # テスト対象コンポ名の抽出
    test_target_component_name = test_target_component_yaml.split("/")[-1].split(".")[0]
    # TcInOpenCanGlConvFotMzd

    # yamlの読み込み
    with open(test_target_component_yaml) as stream:
        data = yaml.load(stream)

    # 入力元コンポの抽出
    input_component_list = getInputComponent(data)
    # ['TcInIfCanGlBase', 'TcInIfCanGlMm', 'TcInIfCanGlMzdFot']

    # 生成するCsvReaderのコンポ名を決定
    csvreader_component_name_list = [
        input_component.replace("TcInIf", "TcInTestCsv")
        for input_component in input_component_list
    ]
    # ['TcInTestCsvCanGlBase', 'TcInTestCsvCanGlMm', 'TcInTestCsvCanGlMzdFot']

    # csvreader_generatorの設定ファイルを生成
    output_path_csvreader_generator_setting_yaml = "./output/temp.adas_sdk_proj/impl/App/SilsCompos/tools/csvreader_generator/generate_setting/"
    genCsvReaderGeneratorSettingYaml(
        output_path_csvreader_generator_setting_yaml, csvreader_component_name_list
    )

    # dump設定iniファイルを生成
    output_path_dump_setting_ini = (
        "./output/temp.adas_sdk_proj/bin/property/adas_sdk_dump_setting_test.ini"
    )
    genDumpSettingIni(
        output_path_dump_setting_ini,
        csvreader_component_name_list,
        test_target_component_name,
        test_target_node_name,
    )

    # テスト用のLaunchファイルを生成　※BUILD.bazelへのadas_sdk_binaryへの追記は仕方ない
    output_path_launch_yaml = (
        "./output/temp.adas_sdk_proj/grconf_launch/SilsCompos/open.test.launch.yaml"
    )
    genLaunchYaml(
        output_path_launch_yaml,
        output_path_dump_setting_ini,
        csvreader_component_name_list,
        test_target_component_name,
        test_target_node_name,
    )

    # targets.bzlを生成　※load()などのパスはOEMリポごとに異なる
