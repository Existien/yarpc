/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/07_qml_instantiation.yml
 *   Object: QmlStruct
 *   Template: qt6/struct_source.j2
 */
#include <QMetaType>
#include <QDBusMetaType>
#include "QmlStruct.hpp"
#include "types.hpp"

using namespace gen::qml_instantiation;

QDBusArgument &gen::qml_instantiation::operator<<(QDBusArgument &argument, const QmlStruct &object) {
    argument.beginStructure();
    argument << object.content;
    argument << object.number;
    argument << *reinterpret_cast<const int*>(&object.someEnum);
    argument.endStructure();
    return argument;
}

const QDBusArgument &gen::qml_instantiation::operator>>(const QDBusArgument &argument, QmlStruct &object) {
    argument.beginStructure();
    argument >> object.content;
    argument >> object.number;
    int dbusSomeEnum;
    argument >> dbusSomeEnum;
    object.someEnum = *reinterpret_cast<const QmlEnum::Type*>(&dbusSomeEnum);
    argument.endStructure();
    return argument;
}

bool gen::qml_instantiation::operator!=(const QmlStruct &lhs, const QmlStruct &rhs) {
    return (false
        || lhs.content != rhs.content
        || lhs.number != rhs.number
        || lhs.someEnum != rhs.someEnum
    );
}

QmlStruct QmlStructFactory::create (
    QString content,
    double number,
    QmlEnum::Type someEnum
) const {
    return QmlStruct {
        .content = content,
        .number = number,
        .someEnum = someEnum,
    };
}

QmlStruct QmlStructFactory::create (
    QVariant content,
    QVariant number,
    QVariant someEnum
) const {
    QString member_0;
    member_0 = content.value<QString>();

    double member_1;
    member_1 = number.value<double>();

    QmlEnum::Type member_2;
    member_2 = someEnum.value<QmlEnum::Type>();

    return QmlStruct {
        .content = member_0,
        .number = member_1,
        .someEnum = member_2,
    };
}