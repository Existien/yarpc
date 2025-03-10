/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.2_dictionaries_with_structs.yml
 *   Object: SimonsDict
 *   Template: qt6/struct_source.j2
 */
#include <QMetaType>
#include <QDBusMetaType>
#include "SimonsDict.hpp"
#include "types.hpp"

using namespace gen::dicts;

QDBusArgument &gen::dicts::operator<<(QDBusArgument &argument, const SimonsDict &object) {
    argument.beginStructure();
    argument << object.numbers;
    argument.endStructure();
    return argument;
}

const QDBusArgument &gen::dicts::operator>>(const QDBusArgument &argument, SimonsDict &object) {
    argument.beginStructure();
    argument >> object.numbers;
    argument.endStructure();
    return argument;
}

bool gen::dicts::operator!=(const SimonsDict &lhs, const SimonsDict &rhs) {
    return (false
        || lhs.numbers != rhs.numbers
    );
}

SimonsDict SimonsDictFactory::create (
    QMap<QString, StructDict> numbers
) const {
    return SimonsDict {
        .numbers = numbers,
    };
}

SimonsDict SimonsDictFactory::create (
    QVariant numbers
) const {
    QMap<QString, StructDict> member_0;
    member_0 = numbers.value<QMap<QString, StructDict>>();

    return SimonsDict {
        .numbers = member_0,
    };
}